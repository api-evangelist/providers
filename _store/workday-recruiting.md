---
aid: workday-recruiting
url: https://raw.githubusercontent.com/api-evangelist/workday-recruiting/refs/heads/main/apis.yml
apis:
- name: Workday Recruiting REST API
  description: RESTful API for managing recruiting operations including job requisitions, candidates, applications, and hiring processes in Workday. Supports OAuth 2.0 authentication and returns data in JSON format for integration with talent management and applicant tracking systems.
  image: https://www.workday.com/content/dam/web/images/logos/workday-logo.svg
  humanURL: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
  baseURL: https://wd2-impl-services1.workday.com/ccx/api/recruiting/
  tags:
  - Applications
  - Candidates
  - Job Requisitions
  - Recruiting
  - Talent Acquisition
  properties:
  - type: Documentation
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html
  - type: OpenAPI
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Recruiting/v41.2/Recruiting_OpenAPI.yaml
  - type: Authentication
    url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#authentication
  - type: Rate Limits
    url: https://community.workday.com/articles/16827
- name: Workday Recruiting SOAP Web Services API
  description: SOAP-based web service providing comprehensive access to Workday Recruiting business services data for integration with talent management and applicant tracking systems. Includes over 120 operations covering candidate management, job requisitions, evergreen requisitions, job postings, interviews, background checks, recruiting agencies, and self-schedule calendars.
  image: https://www.workday.com/content/dam/web/images/logos/workday-logo.svg
  humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Recruiting/v45.2/Recruiting.html
  baseURL: https://wd2-impl-services1.workday.com/ccx/service/
  tags:
  - Candidates
  - Job Requisitions
  - Recruiting
  - SOAP API
  - Web Services
  properties:
  - type: Documentation
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Recruiting/v45.2/Recruiting.html
  - type: Reference
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
  - type: Change Log
    url: https://community.workday.com/api-versions
name: Workday Recruiting
tags:
- HCM
- Human Resources
- Recruiting
- SaaS
- Talent Acquisition
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for Workday's cloud-based recruiting and talent acquisition solution, providing programmatic access to job requisitions, candidate management, applications, interviews, job postings, and hiring workflows.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

