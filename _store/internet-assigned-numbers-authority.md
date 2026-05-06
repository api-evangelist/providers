---
aid: internet-assigned-numbers-authority
name: Internet Assigned Numbers Authority
description: The Internet Assigned Numbers Authority (IANA) performs the global coordination of the DNS Root, IP addressing, and other Internet protocol resources. IANA maintains the protocol registries, top-level domain delegations, time zone database, and language subtag registry that the Internet relies on. Bulk registry data is published as machine-readable files distributed via rsync and FTP rather than through a public REST API.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Domains
  - DNS
  - IP Addressing
  - Media Types
  - Protocols
  - Standards
  - Time Zones
url: https://raw.githubusercontent.com/api-evangelist/internet-assigned-numbers-authority/refs/heads/main/apis.yml
created: '2025-08-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: internet-assigned-numbers-authority:iana-protocol-registries
    name: IANA Protocol Registries
    description: The IANA Protocol Registries publish the authoritative assignments for Internet protocol parameters. Bulk registry data is available as XML, CSV, and plain-text files distributed via rsync and FTP for programmatic consumption.
    humanURL: https://www.iana.org/protocols
    baseURL: https://www.iana.org/assignments/
    tags:
      - Protocols
      - Standards
      - Registries
    properties:
      - type: Documentation
        url: https://www.iana.org/protocols
      - type: Bulk
        url: rsync://rsync.iana.org/assignments
  - aid: internet-assigned-numbers-authority:iana-time-zone-database
    name: IANA Time Zone Database
    description: The IANA Time Zone Database (tz database) provides the canonical source of time zone and daylight saving rules used by operating systems and applications worldwide. Data and source code are released as tarballs.
    humanURL: https://www.iana.org/time-zones
    baseURL: https://data.iana.org/time-zones/
    tags:
      - Time Zones
      - Standards
    properties:
      - type: Documentation
        url: https://www.iana.org/time-zones
      - type: Bulk
        url: https://data.iana.org/time-zones/releases/
  - aid: internet-assigned-numbers-authority:iana-root-zone-database
    name: IANA Root Zone Database
    description: The Root Zone Database represents the delegation details of top-level domains, including country code (ccTLD) and generic (gTLD) top-level domains.
    humanURL: https://www.iana.org/domains/root/db
    baseURL: https://www.iana.org/domains/
    tags:
      - DNS
      - Domains
      - Registries
    properties:
      - type: Documentation
        url: https://www.iana.org/domains/root/db
common:
  - type: Website
    url: https://www.iana.org/
  - type: GitHub Organization
    url: https://github.com/iana-org
  - type: News
    url: https://www.iana.org/news
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
