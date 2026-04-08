---
aid: nist
url: https://raw.githubusercontent.com/api-evangelist/nist/refs/heads/main/apis.yml
apis:
- aid: nist:nist-nvd-api
  name: NIST National Vulnerability Database (NVD) API
  description: Provides programmatic access to the National Vulnerability Database, including CVE information, vulnerability metrics, and security advisories.
  humanURL: https://nvd.nist.gov/developers
  baseURL: https://services.nvd.nist.gov/rest/json
  tags:
  - CVE
  - Cybersecurity
  - Security
  - Vulnerabilities
  properties:
  - type: Documentation
    url: https://nvd.nist.gov/developers/vulnerabilities
  - type: Authentication
    url: https://nvd.nist.gov/developers/request-an-api-key
- aid: nist:nist-chemistry-webbook-api
  name: NIST Chemistry WebBook API
  description: Access to chemical and physical property data for thousands of chemical species.
  humanURL: https://webbook.nist.gov/chemistry/
  baseURL: https://webbook.nist.gov/cgi
  tags:
  - Chemistry
  - Physical Properties
  - Scientific Data
  properties:
  - type: Documentation
    url: https://webbook.nist.gov/chemistry/form-ser/
- aid: nist:nist-data-gateway
  name: NIST Data Gateway
  description: Provides access to NIST's scientific and technical databases across multiple domains.
  humanURL: https://data.nist.gov
  baseURL: https://data.nist.gov
  tags:
  - Open Data
  - Research Data
  - Scientific Data
  properties:
  - type: Documentation
    url: https://data.nist.gov/sdp/#/
- aid: nist:nist-time-api
  name: NIST Time API
  description: Provides access to official NIST time services for time synchronization.
  humanURL: https://www.nist.gov/pml/time-and-frequency-division/time-distribution/internet-time-service-its
  tags:
  - Standards
  - Synchronization
  - Time
  properties:
  - type: Documentation
    url: https://tf.nist.gov/tf-cgi/servers.cgi
name: National Institute of Standards and Technology (NIST)
tags:
- Cybersecurity
- Government
- Measurements
- Research
- Scientific Data
- Standards
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs provided by the National Institute of Standards and Technology for accessing scientific and technical data, standards, and research information including vulnerability databases, chemistry data, and time services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

