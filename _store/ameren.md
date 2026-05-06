---
aid: ameren
name: Ameren
description: Ameren Corporation is a regulated electric and natural gas utility serving customers in Missouri and Illinois. The company provides reliable energy delivery, smart grid infrastructure, and renewable energy programs. Ameren Illinois implements the Green Button Connect My Data program (Share My Usage) based on the ESPI standard, enabling authorized third parties to access customer energy usage data. Ameren also operates a Renewables Portal for community solar generation owners and participates in grid modernization initiatives.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Utility
  - Energy
  - Electric
  - Natural Gas
  - Smart Grid
  - Green Button
  - Renewable Energy
url: https://raw.githubusercontent.com/api-evangelist/ameren/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: ameren:share-my-usage-api
    name: Ameren Share My Usage API
    description: The Ameren Illinois Share My Usage API implements the Green Button Connect My Data program, providing authorized third parties access to up to 24 months of historical electric energy usage data for residential and small commercial customers via the ESPI (Energy Services Provider Interface) standard. Authentication uses OAuth with customer authorization via Ameren Illinois online accounts. Operated by data custodian Aclara.
    humanURL: https://www.ameren.com/partners/account-and-data/share-my-usage
    baseURL: https://api.ameren.com
    tags:
      - Green Button
      - Energy Data
      - ESPI
      - Smart Meter
      - Data Sharing
    properties:
      - type: Documentation
        url: https://www.ameren.com/partners/account-and-data/share-my-usage
      - type: Authentication
        url: https://www.ameren.com/partners/account-and-data/share-my-usage
  - aid: ameren:renewables-portal-api
    name: Ameren Renewables Portal API
    description: The Ameren Renewables Portal enables generation owners to manage community solar and collectively owned generation facilities, track subscriber accounts, and manage billing usage credits in Illinois. Supports community renewable energy including solar, wind, hydro-electric, fuel cells, and agricultural energy sources.
    humanURL: https://www.ameren.com/service/renewables/developers/renewables-portal
    baseURL: https://anm.ameren.com
    tags:
      - Renewable Energy
      - Community Solar
      - Generation Management
      - Illinois
    properties:
      - type: Documentation
        url: https://www.ameren.com/service/renewables/developers/renewables-portal
      - type: Portal
        url: https://anm.ameren.com/illinois/registration
common:
  - type: Website
    url: https://www.ameren.com/
  - type: Portal
    url: https://www.ameren.com/partners/account-and-data/share-my-usage
  - type: Features
    data:
      - name: Green Button Connect My Data
        description: Standard-based program (ESPI/NAESB) enabling authorized third parties to access customer electric energy usage data with OAuth customer authorization for energy analysis, billing, and research.
      - name: Smart Meter Infrastructure
        description: Advanced smart meter deployment enabling two-way communication, real-time usage monitoring, and automated data collection for Illinois and Missouri service territories.
      - name: Community Solar Renewables Portal
        description: Online portal for community solar and generation owners to manage subscriber accounts and billing usage credits in Illinois.
      - name: Outage Management and Restoration
        description: Advanced outage detection, automated notification, and faster power restoration capabilities through smart grid infrastructure.
      - name: Energy Efficiency Programs
        description: Rebates and incentive programs for residential and business customers to reduce energy consumption and improve efficiency.
  - type: UseCases
    data:
      - name: Energy Usage Data Analysis
        description: Authorized third parties access up to 24 months of customer energy usage data for energy efficiency analysis, billing comparisons, and academic research.
      - name: Community Solar Management
        description: Generation owners manage community solar subscriber accounts and billing credits through the Renewables Portal.
      - name: Smart Home Integration
        description: Third-party apps and devices integrate with Ameren usage data via Green Button to provide energy management and automation services.
      - name: Retail Electric Supply Comparison
        description: Retail electric suppliers and comparison platforms access usage data to provide customers with competitive supply options.
  - type: Integrations
    data:
      - name: Green Button Alliance
        description: Ameren Illinois participates in the national Green Button initiative providing standardized energy data access across utilities.
      - name: Aclara
        description: Aclara serves as Ameren Illinois's authorized data custodian for the Share My Usage Green Button program.
      - name: ESPI Standard
        description: Energy Services Provider Interface standard from NAESB for energy usage data exchange in XML format via authenticated API.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
