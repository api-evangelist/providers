---
aid: bristol-myers-squibb
url: https://raw.githubusercontent.com/api-evangelist/bristol-myers-squibb/refs/heads/main/apis.yml
name: Bristol Myers Squibb
tags:
  - Pharmaceutical
  - Biopharmaceutical
  - Oncology
  - Immunology
  - Cardiovascular
  - Clinical Trials
  - Digital Health
  - Fortune 500
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-21'
modified: '2026-04-21'
position: Consumer
description: Bristol Myers Squibb (BMS) is a global Fortune 500 biopharmaceutical company committed to discovering, developing, and delivering innovative medicines for patients with serious diseases. BMS focuses on oncology, immunology, cardiovascular, fibrosis, and cell therapy (CAR T). The company operates BMS Study Connect for clinical trial recruitment, a Medical Information portal for healthcare providers, and the BMS Business Development platform for research partnerships and data sharing. BMS actively pursues technology partnerships in protein degradation, advanced treatment modalities, and digital health.
apis:
  - aid: bristol-myers-squibb:medical-information-api
    name: BMS Medical Information Portal
    tags:
      - Medical Information
      - Healthcare Providers
      - Clinical Data
    humanURL: https://www.bms.com/healthcare-providers/medical-information.html
    properties:
      - url: https://www.bms.com/healthcare-providers/medical-information.html
        type: Portal
    description: The BMS Medical Information portal provides US healthcare providers with access to product medical information, clinical data, and scientific resources for BMS medicines across oncology, immunology, and cardiovascular therapeutic areas.
  - aid: bristol-myers-squibb:study-connect
    name: BMS Study Connect
    tags:
      - Clinical Trials
      - Patient Recruitment
      - Research
    humanURL: https://www.bmsstudyconnect.com/
    properties:
      - url: https://www.bmsstudyconnect.com/
        type: Portal
    description: BMS Study Connect is a clinical trial recruitment and information platform enabling patients and caregivers to find and enroll in Bristol Myers Squibb sponsored clinical research studies.
common:
  - type: Website
    url: https://www.bms.com
  - type: ResearchDataSharing
    url: https://www.bms.com/researchers-and-partners/independent-research/data-sharing-request-process.html
  - type: BusinessDevelopment
    url: https://www.bms.com/researchers-and-partners/business-development.html
  - type: InvestorRelations
    url: https://investors.bms.com
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
