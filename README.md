
# Event_Tickets_Data Scraper
The Event Scraper is a web scraping project designed to extract event information such as event name, date, time, venue name, and venue URL from Ticketmaster event pages. This project leverages Scrapy and Playwright to navigate and scrape dynamic web content efficiently.

## Requirements

To run this scraper, you need to have Python and Scrapy installed. If you don't have Scrapy installed, follow the steps below to set up the environment.

### Installation

1. **Install Python**  
   If you don't have Python installed, download and install it from [here](https://www.python.org/downloads/).

2. **Install Scrapy & Playwright**  
   You can install Scrapy using pip. Run the following command in your terminal or command prompt:

   ```bash
   pip install scrapy playwright
   playwright install
   ```
   

3. **Clone the repository**

   If you haven't already, clone the project to your local machine:

   ```bash
   git clone https://github.com/harshilhh/Event-Scrapper.git
   ```

4. **Navigate to the project directory**

   ```bash
   cd Event-Scrapper/
   ```

## Running the Spider

To run the spider and start scraping the data, use the following command:

```bash
scrapy crawl Get_Events -o file_name.csv
```

This will start the scraper and save the scraped data into a CSV file named `file_name.csv`.

### Sample Output

The scraper extracts data in the following JSON format:
```bash
  [
    {
      "Event Url": "https://www.ticketmaster.com/the-rock-orchestra-by-candlelight...",
      "Event Name": "The Rock Orchestra by Candlelight",
      "Event Date Time": "February 23, 2025",
      "Venue Name": "Dow Event Center",
      "Venue Url": "https://www.ticketmaster.com/dow-event-center-tickets..."
    },
    {
      "Event Url": "https://www.ticketmaster.com/leanne-morgan-just-getting-started...",
      "Event Name": "Leanne Morgan: Just Getting Started",
      "Event Date Time": "May 16, 2025",
      "Venue Name": "Dow Event Center",
      "Venue Url": "https://www.ticketmaster.com/dow-event-center-tickets..."
    }
  ]
```

