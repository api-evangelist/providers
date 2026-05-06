---
aid: national-council-on-disability
name: National Council on Disability
description: The National Council on Disability (NCD) is an independent federal agency that advises the President, Congress, and other federal agencies on disability policy and programs. Established in 1978, the NCD promotes equal opportunity, economic self-sufficiency, independent living, and full participation in all areas of society for individuals with disabilities. The agency conducts research, gathers information, and provides recommendations to improve policies, programs, and services. NCD publishes policy reports spanning civil rights, healthcare, transportation, employment, housing, and emergency management for people with disabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Disability
  - Federal Government
  - Policy
  - Civil Rights
  - Healthcare
  - Independent Agency
url: https://raw.githubusercontent.com/api-evangelist/national-council-on-disability/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: national-council-on-disability:ncd-foia-data
    name: National Council on Disability FOIA Data
    description: FOIA-accessible data from the National Council on Disability including performance and results act reports, congressional budget justification reports, financial audit reports, strategic plans, bylaws, stakeholder letters, and all NCD policy reports. Data is available in PDF, XML, CSV, and ZIP formats through the NCD FOIA e-Library.
    humanURL: https://www.ncd.gov/foia/
    baseURL: https://www.ncd.gov
    tags:
      - FOIA
      - Open Data
      - Government Reports
      - Policy
    properties:
      - type: Documentation
        url: https://www.ncd.gov/foia/
      - type: DataAPI
        url: https://www.ncd.gov/foia/
  - aid: national-council-on-disability:ncd-policy-reports
    name: National Council on Disability Policy Reports
    description: Comprehensive archive of NCD policy reports dating back to 1984 covering disability civil rights, healthcare, transportation, employment, housing, financial assistance, and emergency management. Reports include recommendations to the President, Congress, and federal policymakers on national disability policy.
    humanURL: https://www.ncd.gov/reports/
    baseURL: https://www.ncd.gov
    tags:
      - Policy Reports
      - Civil Rights
      - Healthcare
      - Employment
      - Housing
      - Transportation
    properties:
      - type: Documentation
        url: https://www.ncd.gov/reports/
      - type: DataAPI
        url: https://www.ncd.gov/reports/
  - aid: national-council-on-disability:ncd-accountability-data
    name: National Council on Disability Accountability Reports
    description: Performance, accountability, and budget data from the National Council on Disability. Includes Annual Performance Reports, Congressional Budget Justification Reports, financial audits, and EEO policy statements providing transparency into agency operations and resource allocation.
    humanURL: https://www.ncd.gov/accountability/
    baseURL: https://www.ncd.gov
    tags:
      - Accountability
      - Budget
      - Performance
      - Transparency
    properties:
      - type: Documentation
        url: https://www.ncd.gov/accountability/
      - type: DataAPI
        url: https://www.ncd.gov/accountability/congressional-budget-justification-reports/
common:
  - type: Vocabulary
    url: vocabulary/ncd-vocabulary.yaml
  - type: JSONSchema
    url: json-schema/ncd-policy-report-schema.json
  - type: JSONSchema
    url: json-schema/ncd-foia-record-schema.json
  - type: JSONSchema
    url: json-schema/ncd-accountability-report-schema.json
  - type: JSONSchema
    url: json-schema/ncd-testimony-schema.json
  - type: JSONSchema
    url: json-schema/ncd-stakeholder-letter-schema.json
  - type: Website
    url: https://www.ncd.gov
  - type: Documentation
    url: https://www.ncd.gov/reports/
  - type: DataAPI
    url: https://www.ncd.gov/foia/
  - type: Contact
    url: https://www.ncd.gov/contact/
  - type: PrivacyPolicy
    url: https://www.ncd.gov/privacy-policy/
  - type: Newsroom
    url: https://www.ncd.gov/newsroom/
  - type: Features
    data:
      - name: Policy Reports Archive
        description: Comprehensive archive of NCD policy reports dating back to 1984 covering all areas of disability policy including civil rights, healthcare, employment, housing, and transportation.
      - name: FOIA e-Library
        description: Proactively published collection of NCD documents including bylaws, performance reports, budget justifications, financial audits, and strategic plans available for public download.
      - name: Congressional Testimony Archive
        description: Archive of NCD testimony before Congress on disability policy issues, providing insight into legislative advocacy and policy recommendations over time.
      - name: Disability Policy Toolkits
        description: Practical toolkits and fact sheets on disability rights and policy topics to help individuals, advocates, and policymakers understand and implement disability-inclusive practices.
      - name: Newsroom and Stakeholder Letters
        description: Press releases, newsroom updates, and letters to federal agency stakeholders documenting NCD's ongoing policy engagement and recommendations.
  - type: UseCases
    data:
      - name: Disability Policy Research
        description: Access NCD's comprehensive reports to research disability policy history, current recommendations, and policy gaps across federal programs and agencies.
      - name: FOIA Document Retrieval
        description: Submit FOIA requests or access the FOIA e-Library to retrieve agency financial, performance, and operational documents.
      - name: Legislative Advocacy
        description: Use NCD testimony archives and policy letters as reference material for disability rights advocacy and legislative engagement.
      - name: Federal Agency Compliance
        description: Access NCD recommendations to understand federal agency obligations under disability rights laws including the ADA, Rehabilitation Act, and other statutes.
      - name: Academic Research
        description: Download NCD policy reports, progress reports, and data for academic research on disability policy, independent living, and civil rights.
  - type: Integrations
    data:
      - name: ADA.gov
        description: NCD's work intersects with the Americans with Disabilities Act guidance provided through ADA.gov maintained by the Department of Justice.
      - name: Disability.gov
        description: NCD recommendations inform resources available through federal disability information portals providing access to government benefits and services.
      - name: data.gov
        description: Federal government open data portal where related disability datasets from agencies like SSA, HHS, and DOL are cataloged and made available for download.
      - name: USASpending.gov
        description: NCD federal spending data is publicly accessible through USASpending.gov as part of federal transparency requirements.
  - type: Solutions
    data:
      - name: Disability Policy Leadership
        description: NCD provides independent policy analysis and recommendations to the three branches of government on all matters affecting people with disabilities.
      - name: Federal Agency Accountability
        description: NCD monitors federal agency compliance with disability rights laws and makes recommendations for program improvements and new legislation.
      - name: Public Education
        description: NCD publishes toolkits, fact sheets, and reports to educate the public and policymakers about disability rights and best practices for inclusion.
  - type: JSONLD
    url: json-ld/ncd-context.jsonld
  - type: JSONStructure
    url: json-structure/ncd-policy-report-structure.json
  - type: JSONStructure
    url: json-structure/ncd-foia-record-structure.json
  - type: JSONStructure
    url: json-structure/ncd-accountability-report-structure.json
  - type: JSONStructure
    url: json-structure/ncd-testimony-structure.json
  - type: JSONStructure
    url: json-structure/ncd-stakeholder-letter-structure.json
  - type: Example
    url: examples/ncd-policy-report-example.json
  - type: Example
    url: examples/ncd-foia-record-example.json
  - type: Example
    url: examples/ncd-accountability-report-example.json
  - type: Example
    url: examples/ncd-testimony-example.json
  - type: Example
    url: examples/ncd-stakeholder-letter-example.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
