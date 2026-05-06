---
aid: customs-and-border-protection
name: Customs and Border Protection
x-type: government
description: U.S. Customs and Border Protection (CBP) is the federal law enforcement agency within the Department of Homeland Security responsible for apprehending individuals attempting to enter the United States illegally, stemming the flow of illegal drugs and contraband, protecting agricultural and economic interests from harmful pests and diseases, protecting intellectual property, and regulating and facilitating international trade, collecting import duties, and enforcing U.S. trade laws. CBP's primary trade automation systems are the Automated Commercial Environment (ACE), the Automated Export System (AES), AESDirect, the Advance Passenger Information System (APIS / eAPIS), and the Air Cargo Advance Screening (ACAS) program. Trade integrations are predominantly delivered through Electronic Data Interchange (EDI) messaging via ACE, with a small set of CBP web services (e.g., the AESDirect WebLink Inquiry API) exposed for programmatic use.
url: https://raw.githubusercontent.com/api-evangelist/customs-and-border-protection/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: Public
position: Consuming
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - ACE
  - ACAS
  - AES
  - AESDirect
  - APIS
  - Borders
  - Cargo
  - CBP
  - Customs
  - Department of Homeland Security
  - DHS
  - EDI
  - Exports
  - Federal Government
  - Imports
  - International Trade
  - Manifests
  - Single Window
  - Trade Compliance
apis:
  - aid: customs-and-border-protection:apis-eapis
    name: APIS / eAPIS
    description: The Advance Passenger Information System (APIS) collects pre-arrival and pre-departure manifest data on all passengers and crew members flown or sailed into and out of the United States. The eAPIS web portal allows commercial operators and private aircraft and vessel operators to create, manage, and submit APIS manifests. Bulk and partner integrations use UN/EDIFACT PAXLST and CUSRES messages over CBP-approved transmission methods.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cbp.gov/travel/travel-industry-personnel/advance-passenger-information-system
    baseURL: https://eapis.cbp.dhs.gov/
    tags:
      - APIS
      - Border Security
      - Crew
      - eAPIS
      - Manifests
      - Passengers
    properties:
      - type: Documentation
        url: https://www.cbp.gov/travel/travel-industry-personnel/advance-passenger-information-system
      - type: Portal
        url: https://eapis.cbp.dhs.gov/
      - type: FactSheet
        url: https://www.cbp.gov/sites/default/files/assets/documents/2019-Sep/APIS-Fact-Sheet-2019.pdf
  - aid: customs-and-border-protection:ace
    name: Automated Commercial Environment (ACE)
    description: ACE is the U.S. Single Window through which the trade community reports imports and exports and CBP and Partner Government Agencies determine admissibility. Trade users access ACE via the ACE Secure Data Portal (a free web-based interface) and via ACE Electronic Data Interchange (EDI), which uses CBP-approved CAMIR/AESTIR messaging standards. The ACE Portal modernization program completed user access management migration in February 2025.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cbp.gov/trade/automated
    baseURL: https://ace.cbp.dhs.gov/
    tags:
      - ACE
      - Admissibility
      - Cargo
      - EDI
      - Imports
      - PGA
      - Single Window
    properties:
      - type: Documentation
        url: https://www.cbp.gov/trade/automated
      - type: GettingStarted
        url: https://www.cbp.gov/trade/automated/how-to-use-ace
      - type: Portal
        url: https://ace.cbp.dhs.gov/
      - type: Modernization
        url: https://www.cbp.gov/trade/automated/ace-deployments/ace-portal-modernization
      - type: Deployments
        url: https://www.cbp.gov/trade/automated/ace-deployments
  - aid: customs-and-border-protection:aes
    name: Automated Export System (AES)
    description: AES is the system through which exporters file Electronic Export Information (EEI) for goods leaving the United States. AES is integrated with ACE and supports both EDI filings and the AESDirect web filing tool. AESDirect is the free web-based filing application offered by CBP to file EEI directly into AES.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cbp.gov/trade/aes
    baseURL: https://ace.cbp.dhs.gov/
    tags:
      - AES
      - AESDirect
      - EEI
      - Exports
      - Filings
    properties:
      - type: Documentation
        url: https://www.cbp.gov/trade/aes
      - type: AESDirect
        url: https://www.cbp.gov/trade/aes/aesdirect
  - aid: customs-and-border-protection:aesdirect-weblink-inquiry-api
    name: AESDirect WebLink Inquiry API
    description: The AESDirect WebLink Inquiry API allows authorized partners to programmatically query AESDirect filings. CBP provides separate certification (test) and production environments for the API. This is one of the few directly exposed web APIs in CBP's trade portfolio.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cbp.gov/trade/automated/aesdirect-weblink-inquiry-api
    baseURL: https://ace.cbp.dhs.gov/
    tags:
      - AES
      - AESDirect
      - Filings
      - Inquiry
      - WebLink
    properties:
      - type: Documentation
        url: https://www.cbp.gov/trade/automated/aesdirect-weblink-inquiry-api
  - aid: customs-and-border-protection:acas
    name: Air Cargo Advance Screening (ACAS)
    description: ACAS requires inbound air carriers and other eligible parties to submit advance air cargo data to CBP for security risk-based screening prior to loading on aircraft destined for the United States. ACAS data is transmitted via CBP-approved EDI messages.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cbp.gov/border-security/ports-entry/cargo-security/acas
    baseURL: https://ace.cbp.dhs.gov/
    tags:
      - ACAS
      - Advance Data
      - Air Cargo
      - Pre-loading
      - Security
    properties:
      - type: Documentation
        url: https://www.cbp.gov/border-security/ports-entry/cargo-security/acas
common:
  - type: Website
    url: https://www.cbp.gov/
  - type: TradeAutomation
    url: https://www.cbp.gov/trade/automated
  - type: TradeOutreach
    url: https://www.cbp.gov/trade/stakeholder-engagement
  - type: ACEServiceDesk
    url: https://www.cbp.gov/contact/automated-broker-interface-service-desk
  - type: HelpCenter
    url: https://www.help.cbp.gov/
  - type: Newsroom
    url: https://www.cbp.gov/newsroom
  - type: FOIA
    url: https://www.cbp.gov/site-policy-notices/foia
  - type: PrivacyPolicy
    url: https://www.cbp.gov/site-policy-notices/privacy-policy
  - type: Twitter
    url: https://twitter.com/CBP
  - type: LinkedIn
    url: https://www.linkedin.com/company/u-s-customs-and-border-protection/
  - type: YouTube
    url: https://www.youtube.com/user/CustomsBorderProtect
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
