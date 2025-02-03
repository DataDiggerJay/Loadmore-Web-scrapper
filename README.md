

# **LoadMore Web Scraper** 🚀  
A **Selenium & BeautifulSoup-based web scraper** that automates **dynamic content extraction** from websites with "Load More" buttons. This script continuously **clicks the button, scrapes article details, and stores them** in an Excel file, ensuring **incremental backups** to prevent data loss.  

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/DataDiggerJay/Loadmore-Web-scrapper)  
  

## **📌 Features**  

✅ **Automated Scrolling & Clicking** – Handles infinite scrolling & dynamic "Load More" buttons.  
✅ **Customizable Target Website** – Modify `TARGET_URL` to scrape different blogs or news sites.  
✅ **Data Backup & Export** – Saves data incrementally in CSV & outputs the final data in Excel.  
✅ **Headless Mode** – Runs in the background without opening a browser.  
✅ **Efficient & Scalable** – Prevents infinite loops with a click limit (`MAX_CLICKS`).  

---

## **📂 Project Structure**  
```
📦 Loadmore-Web-Scraper
│── 📄 scraper.py          # Main Python script for scraping
│── 📄 requirements.txt    # List of dependencies
│── 📄 README.md           # Project documentation
│── 📄 scraped_articles.xlsx  # Final extracted data (Generated after running the script)
```

---

## **🔧 Setup & Installation**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/DataDiggerJay/Loadmore-Web-scrapper.git
cd Loadmore-Web-scrapper
```

### **2️⃣ Install Dependencies**  
Ensure you have Python **3.7+** installed. Then, run:  
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Scraper**  
Simply execute the script:  
```sh
python scraper.py
```
It will launch a **headless browser**, scrape articles, and store data in an **Excel file (`scraped_articles.xlsx`)**.

---

## **🛠 Customization Guide**  

🔹 **Change Target Website:** Modify the `TARGET_URL` variable in `scraper.py`.  
🔹 **Scrape Different Data:** Adjust the BeautifulSoup selectors to capture other elements.  
🔹 **Adjust Load More Clicks:** Change `MAX_CLICKS` to control how much data is scraped.  
🔹 **Enable Browser View:** Remove the `--headless` option in Selenium settings.  

---

## **📊 Example Output (Excel File)**  
| Title | href | Original Link |
|--------|------|--------------|
| Example Blog Post 1 | https://example.com/post1 | https://example.com/post1 |
| Example Blog Post 2 | https://example.com/post2 | https://example.com/post2 |

---

## **📜 License**  
This project is **MIT Licensed** – feel free to modify and use it for your own projects! 🎯  

---

## **🤝 Contributing**  
Pull requests and improvements are welcome! Feel free to:  
✅ Report Issues  
✅ Add Features  
✅ Improve Documentation  

---

## **🌟 Show Your Support**  
If you found this project useful, please **⭐ Star this repository** and **Share it** with others! 🚀  

---

Happy Scraping! 🕵️‍♂️💻  

---
