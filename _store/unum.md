---
aid: unum
name: Unum
description: Unum Group is a leading provider of financial protection benefits including disability insurance, life insurance, dental insurance, vision insurance, and critical illness coverage. Unum's developer platform offers APIs for HR system integration, eligibility management, leave and absence management, enrollment, and evidence of insurability processing.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Insurance
  - Benefits Administration
  - HR Integration
  - Disability Insurance
  - Life Insurance
url: https://raw.githubusercontent.com/api-evangelist/unum/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: unum:hr-connect
    name: Unum HR Connect API
    description: The Unum HR Connect API provides a secure, real-time connection between Unum benefits and major HR platforms including Workday, ADP, and UKG. It automates eligibility checks, evidence of insurability (EOI), premium billing calculations, leave and absence management, and enrollment data synchronization, eliminating manual EDI batch file processing.
    humanURL: https://www.unum.com/employers/hr-trends/api-integration-with-hr-systems
    baseURL: https://api.unum.com
    tags:
      - HR Integration
      - Benefits Administration
      - Eligibility
      - Enrollment
      - Leave Management
    properties:
      - type: Documentation
        url: https://developer.unum.com/s/
      - type: Website
        url: https://www.unum.com/employers/hr-trends/api-integration-with-hr-systems
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unum/refs/heads/main/openapi/unum-hr-connect-openapi.yml
  - aid: unum:benefits-enrollment
    name: Unum Benefits Enrollment API
    description: The Unum Benefits Enrollment API allows benefits administration platforms and HR systems to submit, update, and manage employee benefit enrollments in real time. The API enables seamless data synchronization between employer HR systems and Unum's benefits administration, supporting life events, open enrollment, and real-time quoting for voluntary benefits.
    humanURL: https://developer.unum.com/s/
    baseURL: https://api.unum.com
    tags:
      - Benefits Enrollment
      - Insurance
      - Voluntary Benefits
    properties:
      - type: Documentation
        url: https://developer.unum.com/s/
      - type: Website
        url: https://www.unum.com/employers/solutions/myunum
  - aid: unum:leave-absence
    name: Unum Leave and Absence Management API
    description: The Unum Leave and Absence Management API integrates Unum's leave solutions directly with HCM platforms, automating leave request intake, status tracking, return-to-work coordination, and FMLA/state leave eligibility determination. The API eliminates manual data entry by connecting leave workflows between employer HR systems and Unum's leave management platform.
    humanURL: https://developer.unum.com/s/
    baseURL: https://api.unum.com
    tags:
      - Leave Management
      - FMLA
      - Absence Management
      - HR Integration
    properties:
      - type: Documentation
        url: https://developer.unum.com/s/
common:
  - type: Website
    url: https://www.unum.com
  - type: Developer Portal
    url: https://developer.unum.com/s/
  - type: Documentation
    url: https://developer.unum.com/s/
  - type: Blog
    url: https://www.unum.com/employers/hr-trends
  - type: Case Studies
    url: https://www.broadcom.com/case-studies/automation/unum-better-leverages-apis-to-deepen-customer-relationships-and-improve-customer-loyalty
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
