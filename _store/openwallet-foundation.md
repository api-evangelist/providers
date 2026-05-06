---
aid: openwallet-foundation
name: OpenWallet Foundation
description: The OpenWallet Foundation is a Linux Foundation Europe project that brings developers and standards organizations together to facilitate global interoperability of verifiable credentials and digital wallet technology. It develops open source engines for secure, privacy-preserving digital identity solutions.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Credentials
  - Digital Wallet
  - Identity
  - Linux Foundation
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/openwallet-foundation/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: openwallet-foundation:aca-py-admin-api
    name: ACA-Py Admin API
    description: Aries Cloud Agent Python (ACA-Py) exposes an OpenAPI-documented REST Admin API used by controller applications to manage agent behavior, issue and verify credentials, exchange messages, and orchestrate DIDComm protocols. The exact set of endpoints is generated dynamically based on the protocols loaded by the running agent.
    humanURL: https://aca-py.org/
    tags:
      - Aries
      - Credentials
      - DIDComm
      - Digital Wallet
      - Identity
    properties:
      - type: Documentation
        url: https://aca-py.org/
      - type: Reference
        url: https://github.com/openwallet-foundation/acapy/blob/main/docs/features/AdminAPI.md
      - type: GitHubRepository
        url: https://github.com/openwallet-foundation/acapy
  - aid: openwallet-foundation:credo-api
    name: Credo API
    description: Credo (formerly Aries Framework JavaScript) is a TypeScript framework for building decentralized identity and verifiable credential applications. It exposes programmatic interfaces for issuing, verifying, and exchanging credentials over DIDComm and OpenID for Verifiable Credentials.
    humanURL: https://credo.js.org/
    tags:
      - Aries
      - Credentials
      - DIDComm
      - Digital Wallet
      - Identity
      - JavaScript
    properties:
      - type: Documentation
        url: https://credo.js.org/
      - type: GitHubRepository
        url: https://github.com/openwallet-foundation/credo-ts
  - aid: openwallet-foundation:askar-api
    name: Askar API
    description: Askar is a secure storage backend for digital wallets that manages cryptographic keys, secrets, and credential records. It provides language bindings (Python, Rust, JavaScript, Kotlin, Swift) for reading and writing wallet entries and performing cryptographic operations.
    humanURL: https://github.com/openwallet-foundation/askar
    tags:
      - Cryptography
      - Digital Wallet
      - Storage
    properties:
      - type: Documentation
        url: https://github.com/openwallet-foundation/askar
      - type: GitHubRepository
        url: https://github.com/openwallet-foundation/askar
  - aid: openwallet-foundation:vc-api
    name: VC API
    description: VC API is an implementation of the W3C Verifiable Credentials API draft standard, exposing REST endpoints for verifiable credential issuance, verification, and presentation exchange.
    humanURL: https://github.com/openwallet-foundation-labs/vc-api
    tags:
      - Credentials
      - Identity
      - Verifiable Credentials
      - W3C
    properties:
      - type: Documentation
        url: https://github.com/openwallet-foundation-labs/vc-api
      - type: Reference
        url: https://w3c-ccg.github.io/vc-api/
      - type: GitHubRepository
        url: https://github.com/openwallet-foundation-labs/vc-api
  - aid: openwallet-foundation:sd-jwt-api
    name: SD-JWT Libraries
    description: OpenWallet Foundation maintains Selective Disclosure for JSON Web Tokens (SD-JWT) libraries across multiple languages including JavaScript, Python, Rust, Kotlin, and .NET. These libraries expose programmatic interfaces for issuing, holding, and verifying SD-JWT and SD-JWT-VC credentials.
    humanURL: https://github.com/openwallet-foundation/sd-jwt-js
    tags:
      - Credentials
      - Cryptography
      - JWT
      - Selective Disclosure
    properties:
      - type: Documentation
        url: https://github.com/openwallet-foundation/sd-jwt-js
      - type: Reference
        url: https://datatracker.ietf.org/doc/draft-ietf-oauth-selective-disclosure-jwt/
      - type: GitHubRepository
        url: https://github.com/openwallet-foundation/sd-jwt-js
common:
  - url: https://openwallet.foundation/
    name: OpenWallet Foundation
    type: Website
    description: Official OpenWallet Foundation website.
  - url: https://openwallet.foundation/projects/
    name: Projects
    type: Documentation
    description: Catalog of OpenWallet Foundation Impact, Growth, and Lab projects.
  - url: https://github.com/openwallet-foundation
    name: GitHub Organization
    type: GitHub Organization
    description: OpenWallet Foundation GitHub organization with project source code.
  - url: https://github.com/openwallet-foundation-labs
    name: GitHub Labs
    type: GitHub Organization
    description: OpenWallet Foundation Labs organization for incubating projects.
  - url: https://openwallet.foundation/blog/
    name: Blog
    type: Blog
    description: OpenWallet Foundation announcements and project updates.
  - url: https://openwallet.foundation/community/
    name: Community
    type: Community
    description: Community resources, working groups, and contribution guidance.
  - url: https://lists.openwallet.foundation/
    name: Mailing Lists
    type: Mailing List
    description: Public mailing lists for OpenWallet Foundation working groups.
  - url: https://openwallet.foundation/about/
    name: About
    type: About
    description: About the OpenWallet Foundation, governance, and members.
  - url: https://openwallet.foundation/privacy-policy/
    name: Privacy
    type: Privacy
    description: OpenWallet Foundation privacy policy.
  - url: https://openwallet.foundation/terms-of-use/
    name: Terms of Service
    type: Terms of Service
    description: OpenWallet Foundation terms of use.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
