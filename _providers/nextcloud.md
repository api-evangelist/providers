---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Nextcloud Agentic Access
  operation_count: 5
  slug: nextcloud-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 6
apis:
- description: Open Collaboration Services REST API for managing shares, users, groups, capabilities, status, notifications, activities, and other Nextcloud server resources. Uses Basic Auth, app passwords, or OAuth
  name: Nextcloud OCS API
  slug: ocs-api
- description: WebDAV interface for files, folders, chunked uploads, trashbin, versions, comments, and search on a Nextcloud server. Provides the primary file-sync protocol used by Nextcloud desktop and mobile clien
  name: Nextcloud WebDAV API
  slug: webdav-api
- description: The Autocomplete API from Nextcloud — 1 operation(s) for autocomplete.
  name: Nextcloud Autocomplete API
  slug: nextcloud-autocomplete-api
- description: The Capabilities API from Nextcloud — 1 operation(s) for capabilities.
  name: Nextcloud Capabilities API
  slug: nextcloud-capabilities-api
- description: The DAV API from Nextcloud — 1 operation(s) for dav.
  name: Nextcloud DAV API
  slug: nextcloud-dav-api
- description: The Users API from Nextcloud — 2 operation(s) for users.
  name: Nextcloud Users API
  slug: nextcloud-users-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nextcloud OCS Autocomplete API
  slug: open-nextcloud-autocomplete-api
- collection_type: open
  name: Nextcloud OCS Autocomplete Capabilities API
  slug: open-nextcloud-capabilities-api
- collection_type: open
  name: Nextcloud OCS Autocomplete DAV API
  slug: open-nextcloud-dav-api
- collection_type: open
  name: Nextcloud OCS Autocomplete Users API
  slug: open-nextcloud-users-api
- collection_type: open
  name: Nextcloud OCS API
  slug: open-nextcloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nextcloud-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nextcloud-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nextcloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nextcloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nextcloud-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nextcloud-gmbh
- group: company
  title: ''
  type: Website
  url: https://nextcloud.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nextcloud.com
- group: docs
  title: ''
  type: Developer Manual
  url: https://docs.nextcloud.com/server/latest/developer_manual/
- group: commercial
  title: ''
  type: Pricing
  url: https://nextcloud.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://nextcloud.com/sign-up/
- group: operate
  title: ''
  type: Support
  url: https://nextcloud.com/support/
- group: company
  title: ''
  type: Blog
  url: https://nextcloud.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nextcloud
- group: build
  title: ''
  type: GitHub Server
  url: https://github.com/nextcloud/server
- group: other
  title: ''
  type: App Store
  url: https://apps.nextcloud.com
created: '2026-05-11'
description: Nextcloud is an open-source, self-hosted productivity platform offering file sync and share, collaboration, communication (Talk, Mail, Calendar, Contacts), and office (Nextcloud Office) features as a privacy-focused alternative to public cloud suites. Hosted in private datacenters or on-premises, Nextcloud is widely used by enterprises, governments, and individuals. The Nextcloud APIs include OCS REST APIs, WebDAV for file/folder operations, CalDAV/CardDAV, and an OpenAPI-described developer surface for apps and integrations.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nextcloud.png
layout: provider
modified: '2026-05-11'
name: Nextcloud
nav: Providers
network: true
overview: 'Nextcloud publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Capabilities API, DAV API, and 1 more. Tagged areas include File Sync, File Sharing, Collaboration, Self-Hosted, and Open-Source.


  Nextcloud''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 10 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 32.0
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 32.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nextcloud/refs/heads/main/screenshots/nextcloud-2026-06-20T190256.png
security:
- kind: authentication
  name: Nextcloud Authentication
  slug: nextcloud-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Nextcloud Domain Security
  slug: nextcloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nextcloud Vulnerability Disclosure
  slug: nextcloud-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Nextcloud Trust Center
  slug: nextcloud-trust-center
  summary_line: ISO 27001, PCI DSS, HIPAA, GDPR
slug: nextcloud
tags:
- File Sync
- File Sharing
- Collaboration
- Self-Hosted
- Open-Source
- Productivity
- WebDAV
website: https://nextcloud.com
---
