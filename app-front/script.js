/*
  --------------------------------------------------------------------------------------
  Função para obter a lista de wines existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getWineList = async () => {
  // Limpa a tabela antes de inserir novos dados 
  // const tableBody = document.getElementById("wineTable");
  // tableBody.innerHTML = ""
    let url = 'http://127.0.0.1:5000/wines';

    fetch(url, {
      method: 'get',
    })
      .then((response) => response.json())
      .then((data) => {
        clearTableRows();
        data.wines.forEach(item => insertList(
            item.id,
            item.name,
            item.wine_type,
            item.fixed_acidity,
            item.volatile_acidity,
            item.citric_acid,
            item.density,
            item.ph,
            item.alcohol,
            item.quality
        ))
      })
      .catch((error) => {
        console.error('Error:', error);
      });
}


/*
  --------------------------------------------------------------------------------------
  Função para buscar estudantes pelo nome
  --------------------------------------------------------------------------------------
*/
const getWineByName = async () => {
  const wineName = document.getElementById('searchInput').value.trim();

  if (!searchInput) {
      alert("Please enter a name to search!");
      getWineList();
      return;
  }

  const url = `http://127.0.0.1:5000/wine?name=`+ encodeURIComponent(wineName);
  try{
    const response = await fetch(url, {
      method: 'get'
    });
    if(response.status === 200){
      response.json().then((data) => {
        clearTableRows();
        insertList(
            data.id,
            data.name,
            data.wine_type,
            data.fixed_acidity,
            data.volatile_acidity,
            data.citric_acid,
            data.density,
            data.ph,
            data.alcohol,
            data.quality
        );
      })
    }else if(response.status === 404){
      alert("No wines found with the given name.");
      clearSearch();
    }
  }catch(error){
    console.error('Error:', error);
    alert("An error occurred while searching for wines.");
  }

};

/*
  --------------------------------------------------------------------------------------
  Função para colocar um wine na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postWine = async (inputName, inputWineType, inputFixedAcidity, inputVolatileAcidity, inputCitricAcid, inputResidualSugar, inputChlorides, inputFreeSulfurDioxide, inputTotalSulfurDioxide, inputDensity, inputPh, inputSulphates, inputAlcohol) => {
  const formData = new FormData();
  formData.append('name', inputName);
  formData.append('wine_type', inputWineType);
  formData.append('fixed_acidity', inputFixedAcidity);
  formData.append('volatile_acidity', inputVolatileAcidity);
  formData.append('citric_acid', inputCitricAcid);
  formData.append('residual_sugar', inputResidualSugar);
  formData.append('chlorides', inputChlorides);
  formData.append('free_sulfur_dioxide', inputFreeSulfurDioxide);
  formData.append('total_sulfur_dioxide', inputTotalSulfurDioxide);
  formData.append('density', inputDensity);
  formData.append('ph', inputPh);
  formData.append('sulphates', inputSulphates);
  formData.append('alcohol', inputAlcohol);

  console.log("FormData being sent:");
  for (const [key, value] of formData.entries()) {
      console.log(`${key}: ${value}`);
  }

  let url = 'http://127.0.0.1:5000/wine';

  try {
    const response = await fetch(url, {
      method: 'POST',
      body: formData
    });
    console.log(response.status)
    if (response.ok) {
      alert("Wine added successfully!");
    } else if (response.status === 409) {
      alert("Cpf already been added!");
    } else if (response.status === 400) {
      const errorData = await response.json();
      alert(`Error: ${errorData.message || 'Bad request'}`);
    } else {
      alert("Wine not added. Try again.");
    }
  } catch (error) {
    console.error('Error:', error);
    alert("Error trying to add the wine. Please try again later.");
  }
};

/*
  --------------------------------------------------------------------------------------
  Função para Alterar um wine da lista do servidor via requisição Put
  --------------------------------------------------------------------------------------
*/
// const putWine = async (inputName, inputWineType, inputFixedAcidity, inputVolatileAcidity, inputCitricAcid, inputResidualSugar, inputChlorides, inputFreeSulfurDioxide, inputTotalSulfurDioxide, inputDensity, inputPh, inputSulphates, inputAlcohol) => {

//   const formData = new FormData();

//   formData.append('name', inputName);
//   formData.append('wine_type', inputWineType);
//   formData.append('fixed_acidity', inputFixedAcidity);
//   formData.append('volatile_acidity', inputVolatileAcidity);
//   formData.append('citric_acid', inputCitricAcid);
//   formData.append('residual_sugar', inputResidualSugar);
//   formData.append('chlorides', inputChlorides);
//   formData.append('free_sulfur_dioxide', inputFreeSulfurDioxide);
//   formData.append('total_sulfur_dioxide', inputTotalSulfurDioxide);
//   formData.append('density', inputDensity);
//   formData.append('ph', inputPh);
//   formData.append('sulphates', inputSulphates);
//   formData.append('alcohol', inputAlcohol);

//   const url = 'http://127.0.0.1:5000/wine?name=' + encodeURIComponent(wineName);

//   fetch(url, {
//     method: 'put',
//     body: formData
//   })
//   .then((response) => response.json())
//   .catch((error) => {
//     console.error('Error:', error);
//   });
// }

/*
  --------------------------------------------------------------------------------------
  Função para deletar um wine da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteWine = (wineName) => {
  
  let url = 'http://127.0.0.1:5000/wine?name=' + encodeURIComponent(wineName);
  fetch(url, {
    method: 'delete'
  })
  .then((response) => response.json())
  .catch((error) => {
    console.error('Error:', error);
  });
}

/*
  --------------------------------------------------------------------------------------
  Função para limpar o campo de busca e exibir todos os estudantes
  --------------------------------------------------------------------------------------
*/
const clearSearch = () => {
  document.getElementById('searchInput').value = ""; // Limpa o campo de busca
  getWineList(); // Retorna todos os estudantes
};

/*
  --------------------------------------------------------------------------------------
  Função para criar um botão com evento
  --------------------------------------------------------------------------------------
*/
const createButton = (text, className, onClickAction) => {
  const button = document.createElement("button");
  button.textContent = text;
  button.className = className;
  button.onclick = onClickAction;
  return button;
};

/*
  --------------------------------------------------------------------------------------
  Função para preparar o formulário de cadastro do studnet
  --------------------------------------------------------------------------------------
*/
const postWineForm = async () => {
  console.log("postWineForm called");
  let inputName = document.getElementById('name').value.trim();
  let inputWineType = document.getElementById('wine_type').value.trim();
  let inputFixedAcidity = document.getElementById('fixed_acidity').value.trim();
  let inputVolatileAcidity = document.getElementById('volatile_acidity').value.trim();
  let inputCitricAcid = document.getElementById('citric_acid').value.trim();
  let inputResidualSugar = document.getElementById('residual_sugar').value.trim();
  let inputChlorides = document.getElementById('chlorides').value.trim();
  let inputFreeSulfurDioxide = document.getElementById('free_sulfur_dioxide').value.trim();
  let inputTotalSulfurDioxide = document.getElementById('total_sulfur_dioxide').value.trim();
  let inputDensity = document.getElementById('density').value.trim();
  let inputPh = document.getElementById('ph').value.trim();
  let inputSulphates = document.getElementById('sulphates').value.trim();
  let inputAlcohol = document.getElementById('alcohol').value.trim();

  inputWineType = inputWineType.toString();

  if (!inputName) {
    alert("Please enter the wine's name!");
    return;
  } 

  if(inputWineType == 'select'  ){
    alert("Please select the wine's type.");
    return;
  } 
  if (!inputFixedAcidity || isNaN(inputFixedAcidity)) {
    alert("Please enter a valid fixed acidity value.");
    return;
  }
  if (!inputVolatileAcidity || isNaN(inputVolatileAcidity)) {
    alert("Please enter a valid volatile acidity value.");
    return;
  }
  if (!inputCitricAcid || isNaN(inputCitricAcid)) {
    alert("Please enter a valid citric acid value.");
    return;
  }
  if (!inputResidualSugar || isNaN(inputResidualSugar)) {
    alert("Please enter a valid residual sugar value.");
    return;
  }
  if (!inputChlorides || isNaN(inputChlorides)) {
    alert("Please enter a valid chlorides value.");
    return;
  }
  if (!inputFreeSulfurDioxide || isNaN(inputFreeSulfurDioxide)) {
    alert("Please enter a valid free sulfur dioxide value.");
    return;
  }
  if (!inputTotalSulfurDioxide || isNaN(inputTotalSulfurDioxide)) {
    alert("Please enter a valid total sulfur dioxide value.");
    return;
  }
  if (!inputDensity || isNaN(inputDensity)) {
    alert("Please enter a valid density value.");
    return;
  }
  if (!inputPh || isNaN(inputPh)) {
    alert("Please enter a valid pH value.");
    return;
  }
  if (!inputSulphates || isNaN(inputSulphates)) {
    alert("Please enter a valid sulphates value.");
    return;
  }
  if (!inputAlcohol || isNaN(inputAlcohol)) {
    alert("Please enter a valid alcohol value.");
    return;
  }

  await postWine(inputName, inputWineType, inputFixedAcidity, inputVolatileAcidity, inputCitricAcid, inputResidualSugar, inputChlorides, inputFreeSulfurDioxide, inputTotalSulfurDioxide, inputDensity, inputPh, inputSulphates, inputAlcohol);
  clearTableRows();
  getWineList(); // Atualiza a lista de wines após a inserção
}

/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (id, name, wineType, fixedAcidity, volatileAcidity, citricAcid,  density, ph,  alcohol, quality) => {
  const table = document.getElementById("wineTable");
  const row = table.insertRow();
  row.setAttribute("tabindex", "0")

  // Adiciona células de texto com os dados do vinho
  const wineData = [name, wineType, fixedAcidity, volatileAcidity, citricAcid, density, ph, alcohol, quality];
  wineData.forEach(data => {
      const cell = row.insertCell();
      cell.textContent = data;
      cell.setAttribute("tabindex", "0");
  });

  // Adiciona os botões de ação
  const actionsCell = row.insertCell();
  insertButtons(actionsCell, id, name);
  
  // Limpa os campos do formulário
  document.getElementById("name").value = "";
  document.getElementById("wine_type").value = "select";
  document.getElementById("fixed_acidity").value = "";
  document.getElementById("volatile_acidity").value = "";
  document.getElementById("citric_acid").value = "";
  document.getElementById("residual_sugar").value = "";
  document.getElementById("chlorides").value = "";
  document.getElementById("free_sulfur_dioxide").value = "";
  document.getElementById("total_sulfur_dioxide").value = "";
  document.getElementById("density").value = "";
  document.getElementById("ph").value = "";
  document.getElementById("sulphates").value = "";
  document.getElementById("alcohol").value = "";
};

/*
  --------------------------------------------------------------------------------------
  Função para inserir os botões de save e delete, com suas respectivas funções, para cada wine da lista
  --------------------------------------------------------------------------------------
*/
const insertButtons = (parent, wineId,wineName) => {
  // Criação do botão excluir
  const deleteButton = createButton("Delete", "delete-btn", () => {
      if (confirm("Você tem certeza?")) {
          handleDeleteAction(wineName, parent.parentElement);
      }
  });

  // Adicionar botões ao elemento pai
  parent.appendChild(deleteButton);
};

/*
  --------------------------------------------------------------------------------------
  Função para deletar aluno (chamada no evento do botão Delete)
  --------------------------------------------------------------------------------------
*/
const handleDeleteAction = (wineName, rowElement) => {
  if (confirm("Are you sure you want to delete this wine?")) {
    deleteWine(wineName);
    rowElement.remove();
    alert("Wine removed successfully!");
}
};

const clearTableRows = () => {
  const table = document.getElementById('wineTable');  // Substitua 'myTable' pelo id da sua tabela
  const rows = table.getElementsByTagName('tr');

  // Começa do índice 1 para não remover o título (primeira linha)
  for (let i = rows.length - 1; i > 0; i--) {
    table.deleteRow(i);
  }
};

/*
--------------------------------------------------------------------------------------
Chamada da função para carregamento inicial dos dados
--------------------------------------------------------------------------------------
*/
document.addEventListener('DOMContentLoaded', () => {
  // Chama o método para obter a lista de vinhos
  getWineList();
});