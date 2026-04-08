---
aid: adp
url: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/apis.yml
apis:
- aid: adp:adp-workers-api
  name: ADP Workers API
  tags:
  - HCM
  - HR
  - Payroll
  - Workers
  - Workforce
  image: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/image.png
  humanURL: https://developers.adp.com/
  baseURL: https://api.adp.com
  properties:
  - url: https://developers.adp.com/
    type: Documentation
  - url: https://developers.adp.com/articles/guides/workers-management-api-guide-for-adp-expert
    type: Reference
  - url: https://developers.adp.com/getting-started/client-integration-overview
    type: GettingStarted
  - url: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/openapi/adp-workers-openapi.yml
    type: OpenAPI
  description: The ADP Workers API enables access to employee and worker data including personal information, job assignments, pay grades, and employment status. REST APIs support worker lifecycle management for HCM integrations across ADP Workforce Now, Vantage HCM, and Enterprise HR platforms.
- aid: adp:adp-payroll-api
  name: ADP Payroll API
  tags:
  - Compensation
  - CSV
  - HCM
  - HR
  - Payroll
  image: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/image.png
  humanURL: https://developers.adp.com/
  baseURL: https://api.adp.com
  properties:
  - url: https://developers.adp.com/
    type: Documentation
  - url: https://developers.adp.com/articles/guides/payroll-output-api-guide-for-adp-link
    type: Reference
  - url: https://developers.adp.com/getting-started/client-integration-overview
    type: GettingStarted
  - url: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/openapi/adp-payroll-openapi.yml
    type: OpenAPI
  description: The ADP Payroll API provides programmatic access to payroll processing, payroll output data, and compensation management. REST APIs support payroll runs, payroll output retrieval (including CSV-formatted bulk data), and headcount and compensation analysis across ADP payroll platforms.
- aid: adp:adp-embedded-payroll-api
  name: ADP Embedded Payroll API
  tags:
  - Embedded
  - HCM
  - Payroll
  - Small Business
  image: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/image.png
  humanURL: https://developers.adp.com/getting-started/embedded-payroll
  baseURL: https://api.adp.com
  properties:
  - url: https://developers.adp.com/getting-started/embedded-payroll
    type: Documentation
  - url: https://developers.adp.com/getting-started/embedded-payroll
    type: GettingStarted
  description: The ADP Embedded Payroll API enables ISVs and platforms to embed ADP payroll capabilities directly into their applications. REST APIs support payroll processing, tax compliance, and workforce management embedded within partner software products.
- aid: adp:adp-benefits-api
  name: ADP Benefits Administration API
  tags:
  - Benefits
  - Enrollment
  - HCM
  - HR
  image: https://raw.githubusercontent.com/api-evangelist/adp/refs/heads/main/image.png
  humanURL: https://developers.adp.com/
  baseURL: https://api.adp.com
  properties:
  - url: https://developers.adp.com/
    type: Documentation
  description: The ADP Benefits Administration API provides access to employee benefits enrollment, eligibility, and plan data. APIs support benefits carrier connectivity, open enrollment workflows, and benefits data exchange for insurance carriers and benefits administrators.
name: Adp
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: ADP (Automatic Data Processing) is a global provider of cloud-based human capital management solutions including payroll, benefits, talent, time, tax, and HR services for businesses of all sizes.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

