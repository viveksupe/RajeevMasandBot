# Rajeev Masand Review Scraper Slack Bot

The goal of this project is to retrieve review rating for Bollywood & Hollywood movies given by Indian movie critique on rajeevmasand.com and push it to Slack.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
docker
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
cd <Project Directory>
docker build -t rajeevbot .
docker run  --name RajeevBot -e SLACK_URL='WEBHOOK_URL' rajeevbot
```

Cron Job

```
0 19 * * 5 docker start RajeevBot
```

Webhook Content:
```
Bollywood:
--------------------------------------------------
Long and short of it: Zero
    Rating: 2
--------------------------------------------------
--------------------------------------------------
Iceberg up ahead!: Kedarnath
    Rating: 2.5
--------------------------------------------------
--------------------------------------------------
Victory of vision: 2.0
    Rating: 3
--------------------------------------------------
--------------------------------------------------
Kid (un)friendly: Pihu
    Rating: 2
--------------------------------------------------
--------------------------------------------------
Sinking ship: Thugs of Hindostan
    Rating: 2
--------------------------------------------------
--------------------------------------------------
Old stock: Baazaar
    Rating: 2.5
--------------------------------------------------
--------------------------------------------------
London bawling!: Namaste England
    Rating: 0
--------------------------------------------------
--------------------------------------------------
Baby bother!: Badhaai Ho
    Rating: 3.5
--------------------------------------------------
--------------------------------------------------
Mother smother: Helicopter Eela
    Rating: 2
--------------------------------------------------
--------------------------------------------------
Horror high!: Tumbbad
    Rating: 3.5
--------------------------------------------------
```
