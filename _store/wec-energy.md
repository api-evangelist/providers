---
aid: wec-energy
name: WEC Energy Group
description: 'WEC Energy Group (NYSE: WEC) is one of the nation''s premier energy companies, serving 4.4 million customers across Wisconsin, Illinois, Michigan, and Minnesota with electricity and natural gas service. The company operates through regional utilities including We Energies, Wisconsin Public Service, Peoples Gas, North Shore Gas, Minnesota Energy Resources, Michigan Gas Utilities, and Upper Michigan Energy Resources. WEC Energy Group offers customer-facing digital services including account management portals, mobile apps, and Green Button energy usage data access.'
image: https://www.wecenergygroup.com/images/wec-logo.png
url: https://raw.githubusercontent.com/api-evangelist/wec-energy/refs/heads/main/apis.yml
created: '2024'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - name: WEC Energy Group Customer Portal API
    description: Web and mobile API powering the WEC Energy Group customer self-service portal. Enables customers to view account information, pay bills, manage alerts, view energy usage history, and report outages. Accessible via the We Energies and Wisconsin Public Service customer websites and mobile apps.
    humanUrl: https://www.we-energies.com/
    tags:
      - Account Management
      - Bill Payment
      - Customer Portal
      - Energy Usage
      - Outage Reporting
    properties:
      - type: Customer Portal
        url: https://www.we-energies.com/customer-service/account-management/
      - type: Mobile App iOS
        url: https://apps.apple.com/us/app/we-energies/id1475985561
      - type: Mobile App Android
        url: https://play.google.com/store/apps/details?id=com.wecenergygroup.we
  - name: Green Button Energy Usage Data API
    description: Green Button is a standardized API for accessing customer energy usage data. Based on the ESPI (Energy Services Provider Interface) standard, it allows customers to authorize third-party applications to access their electricity and gas consumption data. WEC Energy Group utilities support the Green Button Connect My Data standard for automated data sharing.
    humanUrl: https://www.energy.gov/data/green-button
    tags:
      - Energy Data
      - Green Button
      - ESPI
      - OAuth2
      - Smart Meter
      - Usage Data
    properties:
      - type: Documentation
        url: https://dev.greenbuttonalliance.org/
      - type: Standard
        url: https://www.energy.gov/data/green-button
      - type: Open Energy Info
        url: https://openei.org/wiki/Green_Button
  - name: We Energies Outage Map API
    description: Real-time electricity outage information for We Energies service territory in Wisconsin. Provides geographic outage data, estimated restoration times, and affected customer counts. Powers the public-facing outage map.
    humanUrl: https://www.we-energies.com/outages-safety/outages/outage-map/
    tags:
      - Electricity
      - GIS
      - Outage Map
      - Real-Time
      - Wisconsin
    properties:
      - type: Outage Map
        url: https://www.we-energies.com/outages-safety/outages/outage-map/
      - type: Outage Reporting
        url: https://www.we-energies.com/outages-safety/outages/
  - name: Peoples Gas Customer Service API
    description: Customer account and billing API for Peoples Gas, serving natural gas customers in the Chicago metropolitan area. Supports account management, bill payment, usage history, and service requests.
    humanUrl: https://www.peoplesgas.com/
    tags:
      - Account Management
      - Bill Payment
      - Chicago
      - Illinois
      - Natural Gas
    properties:
      - type: Customer Portal
        url: https://www.peoplesgas.com/my-account/
      - type: Website
        url: https://www.peoplesgas.com/
  - name: WEC Energy Group Investor Relations API
    description: 'Financial data and investor relations resources for WEC Energy Group (NYSE: WEC). Provides access to earnings releases, SEC filings, dividend information, stock price data, and annual reports.'
    humanUrl: https://www.wecenergygroup.com/investor-relations/
    tags:
      - Financial Data
      - Investor Relations
      - NYSE
      - SEC Filings
      - Stock Data
    properties:
      - type: Investor Relations
        url: https://www.wecenergygroup.com/investor-relations/
      - type: SEC Filings
        url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000783325
common:
  - type: Website
    url: https://www.wecenergygroup.com
  - type: Customer Portal
    url: https://www.we-energies.com/
  - type: Peoples Gas Portal
    url: https://www.peoplesgas.com/
  - type: Wisconsin Public Service Portal
    url: https://www.wisconsinpublicservice.com/
  - type: Press Room
    url: https://www.wecenergygroup.com/newsroom/
  - type: Investor Relations
    url: https://www.wecenergygroup.com/investor-relations/
  - type: Careers
    url: https://careers.wecenergygroup.com/
  - type: Sustainability
    url: https://www.wecenergygroup.com/sustainability/
  - type: Terms of Service
    url: https://www.we-energies.com/help/legal/terms-of-use/
  - type: Privacy Policy
    url: https://www.wecenergygroup.com/privacy-policy/
  - type: LinkedIn
    url: https://www.linkedin.com/company/wec-energy-group
  - type: Twitter
    url: https://twitter.com/WECEnergyGroup
  - type: Vocabulary
    url: vocabulary/wec-energy-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Energy
  - Electric Utility
  - Fortune 500
  - Green Button
  - Illinois
  - Michigan
  - Minnesota
  - Natural Gas
  - NYSE
  - Utility
  - Wisconsin
---
