---
aid: nvd
name: NVD
description: The National Vulnerability Database (NVD) provides REST APIs for CVE (Common Vulnerabilities and Exposures) data, CPE (Common Platform Enumeration) records, match criteria, and source organizations. APIs deliver vulnerability descriptions, CVSS severity scores, affected product lists, CWE classifications, and reference links for security monitoring and dependency alerting.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Security
  - CVE
  - CPE
  - Vulnerability
  - CVSS
url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/apis.yml
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: nvd:nvd-cve
    name: NVD CVE API
    description: 'The NVD CVE API provides programmatic access to CVE (Common Vulnerabilities and Exposures) records including CVSS severity scores, affected product lists, CWE classifications, and reference links. Supports filtering by CVE ID, CVSS metrics, CWE, keyword, modification date, and publication date. Without an API key: 5 requests per 30 seconds; with key: 50 requests per 30 seconds.'
    humanURL: https://nvd.nist.gov/developers/vulnerabilities
    tags:
      - Security
      - CVE
      - Vulnerability
      - CVSS
    properties:
      - type: Documentation
        url: https://nvd.nist.gov/developers/vulnerabilities
      - type: GettingStarted
        url: https://nvd.nist.gov/developers/start-here
      - type: Authentication
        url: https://nvd.nist.gov/developers/request-an-api-key
      - type: RateLimits
        url: https://nvd.nist.gov/developers/start-here
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/openapi/nvd-cve-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/json-schema/nvd-cve-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/json-ld/nvd-context.jsonld
  - aid: nvd:nvd-cve-history
    name: NVD CVE Change History API
    description: The NVD CVE Change History API tracks modifications to CVE records over time, enabling consumers to identify updated vulnerability data and synchronize their local databases with incremental changes rather than full reloads.
    humanURL: https://nvd.nist.gov/developers/vulnerabilities
    tags:
      - Security
      - CVE
      - Vulnerability
      - Change History
    properties:
      - type: Documentation
        url: https://nvd.nist.gov/developers/vulnerabilities
      - type: GettingStarted
        url: https://nvd.nist.gov/developers/start-here
      - type: Authentication
        url: https://nvd.nist.gov/developers/request-an-api-key
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/openapi/nvd-cve-openapi.yml
  - aid: nvd:nvd-cpe
    name: NVD CPE API
    description: The NVD CPE (Common Platform Enumeration) API provides access to the authoritative CPE dictionary, enabling lookup of software and hardware product identifiers. Supports filtering by CPE name, match string, keyword, and modification date. Returns up to 10,000 results per page.
    humanURL: https://nvd.nist.gov/developers/products
    tags:
      - Security
      - CPE
      - Vulnerability
      - Product Enumeration
    properties:
      - type: Documentation
        url: https://nvd.nist.gov/developers/products
      - type: GettingStarted
        url: https://nvd.nist.gov/developers/start-here
      - type: Authentication
        url: https://nvd.nist.gov/developers/request-an-api-key
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/openapi/nvd-cve-openapi.yml
  - aid: nvd:nvd-cpe-match
    name: NVD CPE Match Criteria API
    description: The NVD CPE Match Criteria API retrieves CPE match strings associated with CVE records, enabling detailed product-to-vulnerability mapping. Supports filtering by CVE ID, match criteria ID, and match string patterns. Returns up to 500 results per page.
    humanURL: https://nvd.nist.gov/developers/products
    tags:
      - Security
      - CPE
      - Vulnerability
      - Match Criteria
    properties:
      - type: Documentation
        url: https://nvd.nist.gov/developers/products
      - type: GettingStarted
        url: https://nvd.nist.gov/developers/start-here
      - type: Authentication
        url: https://nvd.nist.gov/developers/request-an-api-key
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/openapi/nvd-cve-openapi.yml
  - aid: nvd:nvd-source
    name: NVD Source API
    description: The NVD Source API provides information about the organizations that contribute vulnerability data to the NVD dataset, enabling consumers to understand data provenance. Returns up to 1,000 source records per page. Data changes infrequently; once daily updates recommended.
    humanURL: https://nvd.nist.gov/developers/data-sources
    tags:
      - Security
      - CVE
      - Data Sources
      - Organizations
    properties:
      - type: Documentation
        url: https://nvd.nist.gov/developers/data-sources
      - type: GettingStarted
        url: https://nvd.nist.gov/developers/start-here
      - type: Authentication
        url: https://nvd.nist.gov/developers/request-an-api-key
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/openapi/nvd-cve-openapi.yml
  - aid: nvd:nvd-overview
    name: National Vulnerability Database API
    description: The National Vulnerability Database (NVD) provides REST and RSS/Atom APIs for CVE (Common Vulnerabilities and Exposures) data. APIs deliver vulnerability descriptions, CVSS severity scores, affected product lists, and reference links for security monitoring and dependency alerting.
    humanURL: https://nvd.nist.gov/developers
    tags:
      - Security
      - CVE
      - Vulnerability
      - RSS
      - XML
    properties:
      - type: Documentation
        url: https://nvd.nist.gov/developers
common:
  - type: Portal
    url: https://nvd.nist.gov/developers
  - type: Website
    url: https://nvd.nist.gov/
  - type: GettingStarted
    url: https://nvd.nist.gov/developers/start-here
  - type: Authentication
    url: https://nvd.nist.gov/developers/request-an-api-key
  - type: RateLimits
    url: https://nvd.nist.gov/developers/start-here
  - type: TermsOfService
    url: https://nvd.nist.gov/developers/terms-of-use
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/openapi/nvd-cve-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/json-schema/nvd-cve-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/nvd/refs/heads/main/json-ld/nvd-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
