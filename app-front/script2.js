document.addEventListener('DOMContentLoaded', () => {
    const studentTableBody = document.getElementById('studentTableBody');
    const searchInput = document.getElementById('searchInput');
    const addStudentForm = document.getElementById('addStudentForm');

    let students = [];

    // Função para renderizar a lista de alunos
    function renderStudents() {
        studentTableBody.innerHTML = '';

        const filteredStudents = students.filter(student =>
            student.name.toLowerCase().includes(searchInput.value.toLowerCase())
        );

        filteredStudents.forEach((student, index) => {
            const tr = document.createElement('tr');
            
            tr.innerHTML = `
                <td>${student.name}</td>
                <td>${student.cpf}</td>
                <td>${student.gradeLevel}</td>
                <td>${student.matricula}</td>
                <td><input class="student-grade" id="grade1_${index}" type="number" value="${student.grade1}"></td>
                <td><input class="student-grade" id="grade2_${index}" type="number" value="${student.grade2}"></td>
                <td><input class="student-grade" id="grade3_${index}" type="number" value="${student.grade3}"></td>
                <td><input class="student-grade" id="grade4_${index}" type="number" value="${student.grade4}"></td>
                <td>${calculateAverage(student)}</td>
                
                <td>
                    <button class="save-btn" onclick="saveGrades(${index})">Save</button>
                    <button class="delete-btn" onclick="deleteStudent(${index})">Delete</button>
                </td>
            `;
            studentTableBody.appendChild(tr);
        });
    }

    // Função para atualizar nota
    window.updateGrade = (index, grade1, grade2, grade3, grade4) => {
        students[index]['grade1'] = parseFloat(grade1);
        students[index]['grade2'] = parseFloat(grade2);
        students[index]['grade3'] = parseFloat(grade3);
        students[index]['grade4'] = parseFloat(grade4);
        renderStudents();
    };

    // Função para calcular média
    function calculateAverage(aluno) {
        const notas = [aluno.grade1, aluno.grade2, aluno.grade3, aluno.grade4];
        const total = notas.reduce((sum, nota) => sum + nota, 0);
        return (total / notas.length).toFixed(2);
    }

    // Função para salvar notas
    window.saveGrades = (index) => {
        var grade1 = document.getElementById("grade1_" + index).value;
        var grade2 = document.getElementById("grade2_" + index).value;
        var grade3 = document.getElementById("grade3_" + index).value;
        var grade4 = document.getElementById("grade4_" + index).value;

        updateGrade(index,grade1, grade2, grade3, grade4);
        alert(`Notas do aluno ${students[index].nome} salvas com sucesso!`);
    };

    // Função para deletar aluno
    window.deleteStudent = (index) => {
        students.splice(index, 1);
        renderStudents();
    };

    // Função para adicionar novo aluno
    addStudentForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('name').value;
        const cpf = document.getElementById('cpf').value;
        const gradeLevel = document.getElementById('grade-level').value;
        
       console.log(gradeLevel.selectedIndex);
       console.log(gradeLevel.selected);
        const novoAluno = {
            name,
            cpf,
            gradeLevel,
            matricula: `M.${2024}.${students.length + 1}`,
            grade1: 0,
            grade2: 0,
            grade3: 0,
            grade4: 0
        };
        
        students.push(novoAluno);
        renderStudents();

        addStudentForm.reset();
    });

    // Filtragem em tempo real
    searchInput.addEventListener('input', renderStudents);
});


// const insertList = (id, name, cpf, gradeLevel,enrollment,grade1,grade2,grade3,grade4, finalGrade) => {
//   let item = [name, cpf, gradeLevel,enrollment]
//   let table = document.getElementById('studentTable');
//   let row = table.insertRow();

//   for (let i = 0; i < item.length; i++) {
//     let cel = row.insertCell(i);
//     cel.textContent = item[i];
//   }

//   let inputGrade1 = document.createElement("input");
//   inputGrade1.id="grade1_"+id;
//   inputGrade1.className = "student-grade";
//   inputGrade1.type = "number";
//   inputGrade1.value = grade1;

//   let inputGrade2 = document.createElement("input");
//   inputGrade2.id="grade2_"+id;
//   inputGrade2.className = "student-grade";
//   inputGrade2.type = "number";
//   inputGrade2.value = grade2;
  
//   let inputGrade3 = document.createElement("input");
//   inputGrade3.id="grade3_"+id;
//   inputGrade3.className = "student-grade";
//   inputGrade3.type = "number";
//   inputGrade3.value = grade3;  

//   let inputGrade4 = document.createElement("input");
//   inputGrade4.id="grade24_"+id;
//   inputGrade4.className = "student-grade";
//   inputGrade4.type = "number";
//   inputGrade4.value = grade4;



//   row.insertCell(4).appendChild(inputGrade1);
//   row.insertCell(5).appendChild(inputGrade2);
//   row.insertCell(6).appendChild(inputGrade3);
//   row.insertCell(7).appendChild(inputGrade4);
//   let cel = row.insertCell(8);
//   cel.textContent = finalGrade;
//   insertButton(row.insertCell(-1));
  
//   document.getElementById("name").value = "";
//   document.getElementById("cpf").value = "";
//   document.getElementById("grade-level").value = "select";

//   removeElement();
// }

// const updateStudent = () =>{
//   const saveBtn = document.getElementsByClassName("save-btn");

//   for(let i=0; i < saveBtn.length;i++){
//     saveBtn[i].onclick = function(){
//       const div = this.parentElement.parentElement;

//       const studentName = div.getElementsByTagName('td')[0].innerHTML;
//       console.log(i);
//       console.log(studentName);
//       if(confirm("Salvar novas notas?")){
        
//         const rowIndex = i+1;   
//         const inputGrade1 = document.getElementById('grade1_'+rowIndex).value;
//         const inputGrade2 = document.getElementById('grade2_'+rowIndex).value;
//         const inputGrade3 = document.getElementById('grade3_'+rowIndex).value;
//         const inputGrade4 = document.getElementById('grade4_'+rowIndex).value;

//         putStudent(studentName, inputGrade1, inputGrade2, inputGrade3, inputGrade4);
//       }
//     }
//   }
// }


/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão delete
  --------------------------------------------------------------------------------------
*/
// const removeElement = () => {
//   let deleteBtn = document.getElementsByClassName("delete-btn");
//   // var table = document.getElementById('myTable');
//   let i;
//   for (i = 0; i < deleteBtn.length; i++) {
//     deleteBtn[i].onclick = function () {
//       let div = this.parentElement.parentElement;
      
//       const studentName = div.getElementsByTagName('td')[0].innerHTML;

//       console.log(i);
//       console.log(studentName);
//       if (confirm("Você tem certeza?")) {
//         div.remove()
//         deleteStudent(studentName)
//         alert("Removido!")
//       }
//     }
//   }
// }
