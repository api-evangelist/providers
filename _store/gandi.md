---
aid: gandi
name: Gandi
description: Gandi is a domain name registrar and web hosting provider. The Gandi v5 Public API exposes domain management, LiveDNS, certificates, email, organization, billing, and hosting capabilities for programmatic use.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - DNS
  - Domains
  - Domain Registrar
  - Email
  - Hosting
  - Certificates
created: '2025-02-09'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/gandi/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: gandi:domains
    name: Gandi Domain API
    description: The Gandi Domain API enables you to register, manage, transfer, and renew domain names registered with Gandi.
    humanURL: https://api.gandi.net/docs/domains/
    baseURL: https://api.gandi.net/v5/domain
    tags:
      - Domains
      - Domain Registrar
    properties:
      - type: Documentation
        url: https://api.gandi.net/docs/domains/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/gandi/refs/heads/main/openapi/domains-openapi-original.yml
  - aid: gandi:livedns
    name: Gandi LiveDNS API
    description: The Gandi LiveDNS API provides DNS management capabilities for domains managed by Gandi, including DNS records, DNSSEC, zone transfers, and TSIG keys.
    humanURL: https://api.gandi.net/docs/livedns/
    baseURL: https://api.gandi.net/v5/livedns
    tags:
      - DNS
      - Domains
    properties:
      - type: Documentation
        url: https://api.gandi.net/docs/livedns/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/gandi/refs/heads/main/openapi/livedns-openapi-original.yml
  - aid: gandi:certificate
    name: Gandi Certificate API
    description: The Gandi Certificate API allows you to manage SSL/TLS certificates.
    humanURL: https://api.gandi.net/docs/certificate/
    tags:
      - Certificates
      - SSL
    properties:
      - type: Documentation
        url: https://api.gandi.net/docs/certificate/
  - aid: gandi:email
    name: Gandi Email API
    description: The Gandi Email API allows you to manage email accounts and mailboxes.
    humanURL: https://api.gandi.net/docs/email/
    tags:
      - Email
    properties:
      - type: Documentation
        url: https://api.gandi.net/docs/email/
  - aid: gandi:billing
    name: Gandi Billing API
    description: The Gandi Billing API allows you to manage account billing information.
    humanURL: https://api.gandi.net/docs/billing/
    tags:
      - Billing
    properties:
      - type: Documentation
        url: https://api.gandi.net/docs/billing/
  - aid: gandi:organization
    name: Gandi Organization API
    description: The Gandi Organization API allows you to manage organizations and users.
    humanURL: https://api.gandi.net/docs/organization/
    tags:
      - Organization
      - Users
    properties:
      - type: Documentation
        url: https://api.gandi.net/docs/organization/
  - aid: gandi:simplehosting
    name: Gandi Web Hosting API
    description: The Gandi Web Hosting API allows you to manage Simple Hosting instances.
    humanURL: https://api.gandi.net/docs/simplehosting/
    tags:
      - Hosting
    properties:
      - type: Documentation
        url: https://api.gandi.net/docs/simplehosting/
  - aid: gandi:gandicloud
    name: Gandi Cloud VPS API
    description: The GandiCloud VPS API allows you to manage virtual private servers.
    humanURL: https://api.gandi.net/docs/gandicloud/
    tags:
      - Cloud
      - VPS
    properties:
      - type: Documentation
        url: https://api.gandi.net/docs/gandicloud/
common:
  - type: Website
    url: https://www.gandi.net/
  - type: Documentation
    url: https://api.gandi.net/docs/reference/
  - type: Sandbox
    url: https://api.sandbox.gandi.net/docs/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
