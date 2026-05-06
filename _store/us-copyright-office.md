---
aid: us-copyright-office
url: https://raw.githubusercontent.com/api-evangelist/us-copyright-office/refs/heads/main/apis.yml
apis:
  - aid: us-copyright-office:copyright-public-records
    name: Copyright Public Records System
    tags:
      - Copyright
      - Public Records
      - Federal Government
    humanURL: https://publicrecords.copyright.gov/
    properties:
      - url: https://publicrecords.copyright.gov/
        type: Documentation
      - url: https://www.copyright.gov/public-records/
        type: GettingStarted
      - url: https://raw.githubusercontent.com/api-evangelist/us-copyright-office/refs/heads/main/json-schema/us-copyright-office-registration-schema.json
        type: JSONSchema
        title: Copyright Registration Schema
      - url: https://raw.githubusercontent.com/api-evangelist/us-copyright-office/refs/heads/main/json-schema/us-copyright-office-recordation-schema.json
        type: JSONSchema
        title: Copyright Recordation Schema
    description: The Copyright Public Records System (CPRS) provides access to U.S. copyright registration and recordation data with advanced search capabilities and improved interfaces. Replaced the Online Public Catalog in June 2025 and contains records from 1978 onward.
  - aid: us-copyright-office:copyright-bulk-datasets
    name: Copyright Bulk Datasets
    tags:
      - Copyright
      - Bulk Data
      - Federal Government
      - Open Data
    humanURL: https://www.copyright.gov/economic-research/usco-datasets/
    properties:
      - url: https://www.copyright.gov/economic-research/usco-datasets/
        type: Documentation
      - url: https://data.copyright.gov
        type: DataAPI
        title: Bulk Data Download Portal
    description: Bulk download of approximately 22 million U.S. copyright registration records from January 1, 1978 to June 27, 2025. Available in raw unparsed MARC, parsed CSV, and tabular CSV formats. Includes registrations, renewals, cancellations, preregistrations, and recordations across all copyright categories.
  - aid: us-copyright-office:licensing-documents-search
    name: Licensing Documents Search
    tags:
      - Copyright
      - Licensing
      - Federal Government
    humanURL: https://licensing.copyright.gov/lds/
    properties:
      - url: https://licensing.copyright.gov/lds/
        type: Documentation
    description: Searchable directory of licensing documents including compulsory license statements of account, royalty payments, and statutory license records maintained by the Copyright Office.
  - aid: us-copyright-office:dmca-designated-agent
    name: DMCA Designated Agent Directory
    tags:
      - Copyright
      - DMCA
      - Federal Government
    humanURL: https://www.copyright.gov/dmca-directory/
    properties:
      - url: https://www.copyright.gov/dmca-directory/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/us-copyright-office/refs/heads/main/json-schema/us-copyright-office-dmca-agent-schema.json
        type: JSONSchema
        title: DMCA Designated Agent Schema
    description: Searchable directory of Online Service Providers (OSPs) that have registered DMCA designated agents with the U.S. Copyright Office per Section 512 of the Digital Millennium Copyright Act.
name: US Copyright Office
tags:
  - Copyright
  - Federal Government
  - Intellectual Property
  - Open Data
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-03'
position: Consumer
description: The US Copyright Office is a government agency responsible for administering and enforcing copyright laws in the United States. The office is responsible for registering and documenting copyright claims, maintaining the public catalog of copyright records, providing bulk data downloads of registration records, and administering licensing programs. The Copyright Office provides open bulk datasets of approximately 22 million registration records and is modernizing its systems through the Enterprise Copyright System (ECS) program.
common:
  - type: Website
    url: https://www.copyright.gov/
  - type: Documentation
    url: https://www.copyright.gov/public-records/
    title: Search Copyright Records
  - type: DataAPI
    url: https://data.copyright.gov
    title: Bulk Data Downloads
  - type: GettingStarted
    url: https://www.copyright.gov/registration/
    title: Register Your Work
  - type: FAQ
    url: https://www.copyright.gov/eco/faq.html
    title: Online Registration FAQs
  - type: TermsOfService
    url: https://www.copyright.gov/en/about/policies/
    title: Website Policies
  - type: Contact
    url: https://www.copyright.gov/about/contact/
    title: Contact the Copyright Office
  - type: Features
    data:
      - name: Copyright Registration Bulk Data
        description: Approximately 22 million copyright registration records from 1978 to present available for bulk download in MARC, parsed CSV, and tabular CSV formats across all copyright work categories.
      - name: Copyright Public Records System (CPRS)
        description: Advanced search system for copyright registration and recordation data, replacing the Online Public Catalog in June 2025.
      - name: Online Registration (eCO)
        description: Electronic Copyright Office registration system for submitting new copyright registration applications online.
      - name: Licensing Documents Search
        description: Searchable database of compulsory license statements of account and royalty payments filed with the Copyright Office.
      - name: DMCA Designated Agent Directory
        description: Directory of online service providers that have registered DMCA designated agents per Section 512 of the DMCA.
      - name: Enterprise Copyright System Modernization
        description: Ongoing modernization of all Copyright Office IT systems into a unified, interconnected digital infrastructure.
  - type: UseCases
    data:
      - name: Copyright Research and Due Diligence
        description: Searching copyright records to determine ownership, registration status, and rights information for works before licensing or use.
      - name: Bulk Data Analysis and Research
        description: Downloading bulk copyright registration datasets for academic research, legal analysis, or statistical studies of copyright registration trends.
      - name: DMCA Compliance
        description: Looking up DMCA designated agents for online service providers to send takedown notices per Section 512 requirements.
      - name: Licensing Compliance Verification
        description: Searching licensing documents to verify statutory license compliance and royalty payment records.
      - name: Orphan Works Identification
        description: Using copyright records to research ownership of works when rights holders cannot be identified or located.
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/us-copyright-office/refs/heads/main/vocabulary/us-copyright-office-vocabulary.yml
    title: US Copyright Office Vocabulary
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/us-copyright-office/refs/heads/main/json-ld/us-copyright-office-context.jsonld
    title: US Copyright Office JSON-LD Context
  - type: Integrations
    data:
      - name: Library of Congress
        description: Copyright Office is a department of the Library of Congress; data integrates with LC catalog systems and MARC format records.
      - name: U.S. Patent and Trademark Office
        description: Collaborates with USPTO on intellectual property policy, including joint AI and copyright/patent studies.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
