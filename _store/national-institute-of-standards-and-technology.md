---
aid: national-institute-of-standards-and-technology
name: National Institute of Standards and Technology
description: NIST promotes U.S. innovation and industrial competitiveness by advancing measurement science, standards, and technology in ways that enhance economic security and improve our quality of life. NIST operates the National Vulnerability Database (NVD), which provides public APIs for CVE, CVE change history, and CPE records.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-institute-of-standards-and-technology/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Cybersecurity
  - Federal Government
  - Standards
  - Technology
  - Vulnerabilities
apis:
  - aid: national-institute-of-standards-and-technology:nvd-api
    name: NIST National Vulnerability Database (NVD) API
    tags:
      - CVE
      - CPE
      - Cybersecurity
      - Vulnerabilities
    humanURL: https://nvd.nist.gov/developers
    baseURL: https://services.nvd.nist.gov
    properties:
      - url: https://nvd.nist.gov/developers
        type: Documentation
      - url: https://nvd.nist.gov/developers/vulnerabilities
        type: Documentation
      - url: https://nvd.nist.gov/developers/products
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/national-institute-of-standards-and-technology/main/openapi/national-institute-of-standards-and-technology-openapi.yml
        type: OpenAPI
    description: The NVD API provides programmatic access to Common Vulnerabilities and Exposures (CVE) records, CVE change history, and Common Platform Enumeration (CPE) records. Endpoints support pagination, filtering by CVSS metrics, CWE IDs, KEV catalog membership, source identifiers, and publication or modification date ranges.
common:
  - type: Website
    url: https://www.nist.gov/
  - type: Portal
    url: https://nvd.nist.gov/developers
  - type: Documentation
    url: https://nvd.nist.gov/developers/vulnerabilities
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
