const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const PORT = 3000;

app.use(express.json());

let students = [
  { id: 1, name: "Aditya Singh", email: "aditya@example.com", age: 20, course: "Computer Science" },
  { id: 2, name: "Priya Sharma", email: "priya@example.com", age: 21, course: "Data Science" }
];

let nextId = 3; // Counter for auto-generating unique IDs


app.get('/students', (req, res) => {
  // Check if there's an 'id' query parameter
  const { id } = req.query;
  
  if (id) {
    const studentId = parseInt(id);
    const student = students.find(student => student.id === studentId);
    
    if (student) {
      res.json(student);
    } else {
      res.status(404).json({ error: "Student not found" });
    }
  } else {
    // Return all students if no id parameter
    res.json(students);
  }
});

app.post('/students', (req, res) => {
  const { name, email, age, course } = req.body;
  
  // Validate required fields
  if (!name || !email) {
    return res.status(400).json({ error: "Name and email are required" });
  }
  
  // Create new student with auto-generated ID
  const newStudent = {
    id: nextId++,
    name,
    email,
    age: age || null,
    course: course || null
  };
  
  students.push(newStudent);
  res.status(201).json(newStudent);
});

app.put('/students/:id', (req, res) => {
  const studentId = parseInt(req.params.id);
  const { name, email, age, course } = req.body;
  const studentIndex = students.findIndex(student => student.id === studentId);
  
  if (studentIndex !== -1) {
    // Update student but keep the original ID
    students[studentIndex] = {
      id: studentId,
      name: name || students[studentIndex].name,
      email: email || students[studentIndex].email,
      age: age !== undefined ? age : students[studentIndex].age,
      course: course !== undefined ? course : students[studentIndex].course
    };
    res.json(students[studentIndex]);
  } else {
    res.status(404).json({ error: "Student not found" });
  }
});

app.delete('/students/:id', (req, res) => {
  const studentId = parseInt(req.params.id);
  const initialLength = students.length;
  students = students.filter(student => student.id !== studentId);
  
  if (students.length < initialLength) {
    res.status(204).send();
  } else {
    res.status(404).json({ error: "Student not found" });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});