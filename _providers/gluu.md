---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Gluu Agentic Access
  operation_count: 22
  slug: gluu-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 8
apis:
- description: Gluu Flex is the commercial, self-hosted enterprise distribution of the Linux Foundation Janssen Project. It provides a cloud-native digital identity platform with OAuth 2.0, OpenID Connect, FIDO, SCI
  name: Gluu Flex
  slug: gluu-flex
- description: 'The Janssen Project is the upstream Linux Foundation open-source identity platform that powers Gluu Flex. It implements OAuth 2.0, OpenID Connect, FIDO 2.0, SCIM, UMA, and CIBA, providing a federated '
  name: Janssen Project
  slug: janssen-project
- description: Cedarling is an embeddable Policy Decision Point (PDP) built in Rust that runs anywhere and returns authorization decisions in under 50 microseconds based on declarative Cedar access policies. It vali
  name: Cedarling
  slug: cedarling
- description: Agama Lab is a developer portal for authoring Cedar schema and policies, building authentication workflows using the Agama domain specific language, and managing hosted Gluu infrastructure.
  name: Agama Lab
  slug: agama-lab
- description: The discovery API from Gluu — 3 operation(s) for discovery.
  name: Gluu discovery API
  slug: gluu-discovery-api
- description: The fido API from Gluu — 2 operation(s) for fido.
  name: Gluu fido API
  slug: gluu-fido-api
- description: The groups API from Gluu — 3 operation(s) for groups.
  name: Gluu groups API
  slug: gluu-groups-api
- description: The users API from Gluu — 4 operation(s) for users.
  name: Gluu users API
  slug: gluu-users-api
artifact_total: 15
collections:
- collection_type: open
  name: Gluu Flex SCIM 2.0 API
  slug: open-gluu
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gluu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gluu-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gluu-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gluufederation
- group: company
  title: ''
  type: Website
  url: https://gluu.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gluu.org/
- group: company
  title: ''
  type: Blog
  url: https://gluu.org/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.gluu.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GluuFederation
- group: commercial
  title: ''
  type: Pricing
  url: https://gluu.org/pricing/
- group: operate
  title: ''
  type: Contact
  url: https://gluu.org/contact/
- group: operate
  title: ''
  type: Community
  url: https://gluu.org/community/
created: '2025-08-14'
description: Gluu is a technology company that specializes in providing identity and access management solutions for businesses. Their platform allows organizations to centrally manage the authentication and authorization of users across various applications and systems, ensuring secure access to sensitive data and resources.
finops:
- name: Gluu Finops
  service_category: API
  slug: gluu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gluu.png
layout: provider
modified: '2026-04-28'
name: Gluu
nav: Providers
network: true
overview: 'Gluu publishes 4 APIs on the [APIs.io](https://apis.io/) network, including discovery API, fido API, groups API, and 1 more. Tagged areas include Access Management, Authentication, Authorization, IAM, and Identities.


  Gluu''s developer surface includes authentication, documentation, engineering blog, support, pricing, and 7 more developer resources.'
plans:
- name: Gluu Plans Pricing
  plan_count: 3
  slug: gluu-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Gluu Rate Limits
  slug: gluu-rate-limits
score:
  band: thin
  composite: 38.8
  delta: -2.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 49.2
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gluu/refs/heads/main/screenshots/gluu-2026-06-20T181925.png
security:
- kind: authentication
  name: Gluu Authentication
  slug: gluu-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gluu Domain Security
  slug: gluu-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: gluu
tags:
- Access Management
- Authentication
- Authorization
- IAM
- Identities
- OAuth
- OpenID Connect
website: https://gluu.org/
---
