# **Count-Based Snowfall Animation with Peaks**  

This Python project visualizes **gender population data** using **Pygame**. The script:  
- **Creates a snowfall effect** only on the **higher** gender count side.  
- **Displays peaks (mountains)** where:
  - **Big Peak** for the **more populated gender**  
  - **Small Peak** for the **less populated gender**  
  - **Green Peak** for the **higher count**  
  - **Red Peak** for the **lower count**  
- **Uses a black background** to make the peaks stand out.

---

## **How It Works**
- If **males > females**, snowfall appears only on the **left**, and:
  - **Big Green Peak** (left)  
  - **Small Red Peak** (right)  
- If **females > males**, snowfall appears only on the **right**, and:
  - **Big Green Peak** (right)  
  - **Small Red Peak** (left)  
- If **equal**, snowfall appears on **both sides** with **equal green peaks**.

---

## **Project Structure**
```
📦 Gender-Snowfall-Peaks
 ├── genders.csv            # CSV file with gender data
 ├── gender_snowfall.py     # Main Python script
 ├── README.md              # Project documentation
```

---

## **Setup & Installation**
### **1. Install Python & Virtual Environment**
```bash
python -m venv snowfall_ai
source snowfall_ai/bin/activate  # Mac/Linux
snowfall_ai\Scripts\activate     # Windows
```

### **2. Install Dependencies**
```bash
pip install pygame pandas
```

### **3. Run the Animation**
```bash
python gender_snowfall.py
```

---

## **Dataset Used**
The project reads **gender-based population data** from `genders.csv`.


Heres the link : https://github.com/amitness/gender-data/blob/master/genders.csv 


Ensure your CSV file has **three columns**:  
```csv
name,gender,count
aabha,female,3
aabhas,male,2
...
```

---

## **Visual Output**
- **Bigger Green Peak for Higher Population**  
- **Smaller Red Peak for Lower Population**  
- **Snowfall Only on the Higher Count Side**  
- **Black Background for Contrast**  

---

## **License**
This project is **open-source**. Feel free to use and modify it.

