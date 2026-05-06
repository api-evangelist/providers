---
aid: cpanel
name: cPanel
x-type: company
description: cPanel is a web-based control panel that provides a graphical interface and automation tools to simplify the management of web hosting services. cPanel exposes a family of HTTP APIs (UAPI, WHM API 1, and the legacy cPanel API 2) for automating account, domain, email, database, DNS, and server-wide operations. APIs accept API tokens or Basic Authentication and return JSON or XML responses.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/cpanel/refs/heads/main/apis.yml
type: Index
access: 3rd-Party
position: Consuming
created: '2025-02-09'
modified: '2026-04-28'
tags:
  - Control Panel
  - DNS
  - Domains
  - Email
  - Hosting
  - Reseller
  - Server Administration
  - Web Hosting
  - WHM
specificationVersion: '0.19'
apis:
  - aid: cpanel:uapi
    name: cPanel UAPI
    description: The cPanel User API (UAPI) is the modern HTTP API for performing cPanel-level operations such as managing email accounts, mailboxes, files, databases, FTP accounts, SSL certificates, and DNS zones for a single cPanel user. UAPI is the recommended replacement for the legacy cPanel API 2.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://api.docs.cpanel.net/cpanel/introduction/
    baseURL: https://hostname:2083/execute
    tags:
      - Databases
      - Email
      - Files
      - Hosting
      - REST
      - UAPI
    properties:
      - type: Documentation
        url: https://api.docs.cpanel.net/cpanel/introduction/
      - type: GuideToUAPI
        url: https://api.docs.cpanel.net/guides/guide-to-uapi/
      - type: AllUAPIFunctions
        url: https://api.docs.cpanel.net/openapi/cpanel/tag/Email/
      - type: Authentication
        url: https://api.docs.cpanel.net/guides/guide-to-api-authentication/
    features:
      - name: Token Authentication
        description: API tokens scoped per cPanel user.
      - name: Modular Function Catalog
        description: Functions grouped into modules such as Email, DNS, Mysql, and Ftp.
      - name: JSON Responses
        description: Modern JSON responses with consistent metadata envelope.
  - aid: cpanel:whm-api-1
    name: WHM API 1
    description: The WHM API 1 is the HTTP API for server-wide and reseller-level operations including creating, suspending, and terminating cPanel accounts, managing packages and feature lists, configuring DNS clusters, manipulating reseller privileges, and performing system administration.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://api.docs.cpanel.net/whm/introduction/
    baseURL: https://hostname:2087/json-api
    tags:
      - Accounts
      - Packages
      - Reseller
      - Server Administration
      - WHM
    properties:
      - type: Documentation
        url: https://api.docs.cpanel.net/whm/introduction/
      - type: GuideToWHMAPI1
        url: https://api.docs.cpanel.net/guides/guide-to-whm-api-1/
      - type: APIReference
        url: https://api.docs.cpanel.net/openapi/whm/
      - type: Authentication
        url: https://api.docs.cpanel.net/guides/guide-to-api-authentication/
    features:
      - name: Account Management
        description: Create, suspend, terminate, modify, and migrate cPanel accounts.
      - name: Package Management
        description: Define hosting packages and feature lists.
      - name: DNS Cluster Operations
        description: Sync zones across DNS-only servers in a cluster.
  - aid: cpanel:cpanel-api-2
    name: cPanel API 2 (Legacy)
    description: cPanel API 2 is the legacy XML/JSON API for cPanel-user operations. It remains supported for backward compatibility but has been largely superseded by UAPI; new development should target UAPI where possible.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://api.docs.cpanel.net/cpanel/introduction/
    baseURL: https://hostname:2083/json-api/cpanel
    tags:
      - Legacy
      - cPanel
    properties:
      - type: Documentation
        url: https://api.docs.cpanel.net/cpanel/introduction/
      - type: GuideToCPanelAPI2
        url: https://api.docs.cpanel.net/guides/guide-to-cpanel-api-2/
common:
  - type: Website
    url: https://cpanel.net/
  - type: Documentation
    url: https://api.docs.cpanel.net/
  - type: Authentication
    url: https://api.docs.cpanel.net/guides/guide-to-api-authentication/
  - type: ChangeLog
    url: https://api.docs.cpanel.net/whm/release-notes/
  - type: Forum
    url: https://forums.cpanel.net/
  - type: Support
    url: https://support.cpanel.net/
  - type: Status
    url: https://status.cpanel.net/
  - type: GitHub
    url: https://github.com/CpanelInc
  - type: TermsOfService
    url: https://cpanel.net/terms-of-service/
  - type: PrivacyPolicy
    url: https://cpanel.net/privacy-policy/
  - type: LinkedIn
    url: https://www.linkedin.com/company/cpanel
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
