---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: LDAP v3 protocol interface provided by the slapd directory server for reading, writing, and managing hierarchical directory entries. Authentication is via simple bind, SASL mechanisms, or TLS client c
  name: OpenLDAP Directory Service
  slug: ldap-protocol
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openldap-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openldap
- group: company
  title: ''
  type: Website
  url: https://www.openldap.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.openldap.org/doc/
- group: other
  title: ''
  type: Download
  url: https://www.openldap.org/software/download/
- group: operate
  title: ''
  type: FAQ
  url: https://www.openldap.org/faq/
- group: other
  title: ''
  type: Mailing Lists
  url: https://www.openldap.org/lists/
- group: build
  title: ''
  type: Source Code
  url: https://git.openldap.org/openldap/openldap
created: '2026-05-11'
description: OpenLDAP is an open source implementation of the Lightweight Directory Access Protocol (LDAP) that provides directory server daemons, client libraries, and utilities for managing distributed directory services. The suite includes slapd (the standalone LDAP daemon), lloadd (a load balancer), protocol libraries, and command-line tools for searching, modifying, and administering directory data. OpenLDAP does not expose a REST API; access is via the LDAP protocol over TCP using SASL, simple bind, or TLS-secured authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openldap.png
layout: provider
modified: '2026-05-11'
name: OpenLDAP
nav: Providers
network: true
overview: 'OpenLDAP publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Directory Services, LDAP, Identity, Authentication, and Open Source.


  OpenLDAP''s developer surface includes documentation, FAQ, and 6 more developer resources.'
random_paper: 51
score:
  band: minimal
  composite: 8.4
  delta: -2.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openldap/refs/heads/main/screenshots/openldap-2026-06-20T191011.png
security:
- kind: domain-security
  name: Openldap Domain Security
  slug: openldap-domain-security
  summary_line: TLSv1.3 · DMARC
slug: openldap
tags:
- Directory Services
- LDAP
- Identity
- Authentication
- Open Source
- Infrastructure
website: https://www.openldap.org
---
