---
aid: godaddy
name: GoDaddy
description: GoDaddy is a domain registrar and web hosting company offering REST APIs for domain registration, DNS management, certificates, shopper accounts, subscriptions, aftermarket auctions, and abuse reporting.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Aftermarket
  - Certificates
  - DNS
  - Domains
  - Hosting
  - Registrar
url: https://raw.githubusercontent.com/api-evangelist/godaddy/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: godaddy:domains
    name: GoDaddy Domains API
    description: Purchase, renew, transfer, and manage domains, DNS records, contacts, and privacy settings programmatically.
    humanURL: https://developer.godaddy.com/doc/endpoint/domains
    baseURL: https://api.godaddy.com
    tags:
      - Domains
      - DNS
      - Registrar
    properties:
      - type: Documentation
        url: https://developer.godaddy.com/doc/endpoint/domains
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/godaddy/refs/heads/main/openapi/godaddy-domains-openapi.json
  - aid: godaddy:certificates
    name: GoDaddy Certificates API
    description: Issue, validate, renew, and manage SSL/TLS certificates for domains.
    humanURL: https://developer.godaddy.com/doc/endpoint/certificates
    baseURL: https://api.godaddy.com
    tags:
      - Certificates
      - SSL
    properties:
      - type: Documentation
        url: https://developer.godaddy.com/doc/endpoint/certificates
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/godaddy/refs/heads/main/openapi/godaddy-certificates-openapi.json
  - aid: godaddy:shoppers
    name: GoDaddy Shoppers API
    description: Create, retrieve, update, and delete shopper accounts and subaccounts.
    humanURL: https://developer.godaddy.com/doc/endpoint/shoppers
    baseURL: https://api.godaddy.com
    tags:
      - Shoppers
      - Accounts
    properties:
      - type: Documentation
        url: https://developer.godaddy.com/doc/endpoint/shoppers
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/godaddy/refs/heads/main/openapi/godaddy-shoppers-openapi.json
  - aid: godaddy:subscriptions
    name: GoDaddy Subscriptions API
    description: Manage subscription products including listing, canceling, and updating subscription billing settings.
    humanURL: https://developer.godaddy.com/doc/endpoint/subscriptions
    baseURL: https://api.godaddy.com
    tags:
      - Subscriptions
      - Billing
    properties:
      - type: Documentation
        url: https://developer.godaddy.com/doc/endpoint/subscriptions
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/godaddy/refs/heads/main/openapi/godaddy-subscriptions-openapi.json
  - aid: godaddy:orders
    name: GoDaddy Orders API
    description: Retrieve order history, line items, and order details for shopper purchases.
    humanURL: https://developer.godaddy.com/doc/endpoint/orders
    baseURL: https://api.godaddy.com
    tags:
      - Orders
      - Billing
    properties:
      - type: Documentation
        url: https://developer.godaddy.com/doc/endpoint/orders
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/godaddy/refs/heads/main/openapi/godaddy-orders-openapi.json
  - aid: godaddy:aftermarket
    name: GoDaddy Aftermarket API
    description: List, manage, and remove domains for sale on the GoDaddy aftermarket auction platform.
    humanURL: https://developer.godaddy.com/doc/endpoint/aftermarket
    baseURL: https://api.godaddy.com
    tags:
      - Aftermarket
      - Auctions
      - Domains
    properties:
      - type: Documentation
        url: https://developer.godaddy.com/doc/endpoint/aftermarket
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/godaddy/refs/heads/main/openapi/godaddy-aftermarket-openapi.json
  - aid: godaddy:abuse
    name: GoDaddy Abuse API
    description: Submit and track abuse reports related to domains and hosted content.
    humanURL: https://developer.godaddy.com/doc/endpoint/abuse
    baseURL: https://api.godaddy.com
    tags:
      - Abuse
      - Trust and Safety
    properties:
      - type: Documentation
        url: https://developer.godaddy.com/doc/endpoint/abuse
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/godaddy/refs/heads/main/openapi/godaddy-abuse-openapi.json
  - aid: godaddy:agreements
    name: GoDaddy Agreements API
    description: Retrieve legal agreements required for purchasing or registering products.
    humanURL: https://developer.godaddy.com/doc/endpoint/agreements
    baseURL: https://api.godaddy.com
    tags:
      - Agreements
      - Legal
    properties:
      - type: Documentation
        url: https://developer.godaddy.com/doc/endpoint/agreements
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/godaddy/refs/heads/main/openapi/godaddy-agreements-openapi.json
  - aid: godaddy:countries
    name: GoDaddy Countries API
    description: Retrieve supported countries, states, and markets used across GoDaddy APIs.
    humanURL: https://developer.godaddy.com/doc/endpoint/countries
    baseURL: https://api.godaddy.com
    tags:
      - Countries
      - Reference Data
    properties:
      - type: Documentation
        url: https://developer.godaddy.com/doc/endpoint/countries
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/godaddy/refs/heads/main/openapi/godaddy-countries-openapi.json
common:
  - type: Website
    url: https://www.godaddy.com/
  - type: Documentation
    url: https://developer.godaddy.com/doc
  - type: Getting Started
    url: https://developer.godaddy.com/getstarted
  - type: Terms of Service
    url: https://www.godaddy.com/legal/agreements/developer-api-terms
  - type: Support
    url: https://developer.godaddy.com/support
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
