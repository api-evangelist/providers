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
  band: agent-ready
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
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 104
  human_in_the_loop: 0
  name: Escape Agentic Access
  operation_count: 168
  slug: escape-agentic-access
  summary_line: 168 operations · 104 acting
api_count: 20
apis:
- description: Attack Surface Management Trigger and manage ASM discovery scans on your attack surface. See [our documentation](https://docs.escape.tech/documentation/asm/) for more details.
  name: Escape Asm API
  slug: escape-asm-api
- description: Manage every discovered Assets. The public API provide basic CRUDs operations for all available assets. See [our documentation](https://docs.escape.tech/documentation/asm/asset-management/) for more d
  name: Escape Assets API
  slug: escape-assets-api
- description: List audit logs. The public API provides endpoints to list audit logs. See [our documentation](https://docs.escape.tech/documentation/enterprise/audit-logs/) for more details.
  name: Escape Audit API
  slug: escape-audit-api
- description: Beta These endpoints are in beta and are subject to change.
  name: Escape Beta API
  slug: escape-beta-api
- description: Manage your custom rules. The public API provides basic CRUDs operations to manage custom rules. See [our documentation](https://docs.escape.tech/documentation/dast/custom-rules/) for more details.
  name: Escape CustomRules API
  slug: escape-customrules-api
- description: Read scan inbox emails. The public API provides endpoints to list inbox emails and read their raw content without exposing storage links.
  name: Escape Emails API
  slug: escape-emails-api
- description: Manage events. The public API provides basic CRUDs operations to manage events.
  name: Escape Events API
  slug: escape-events-api
- description: Manage 3rd party integrations. The public API provide basic CRUDs operations for all available integrations. See [our documentation](https://https://docs.escape.tech/documentation/asm/integrations/) f
  name: Escape Integrations API
  slug: escape-integrations-api
- description: Manage issues. Identify, prioritize, and remediate the security issues and sensitive data exposures uncovered during ASM and DAST scanning See [our documentation](https://docs.escape.tech/documentatio
  name: Escape Issues API
  slug: escape-issues-api
- description: Asynchronous jobs. Trigger export jobs and poll for completion and artefacts.
  name: Escape Jobs API
  slug: escape-jobs-api
- description: A Location is a proxy environment through which Escape sends requests. The public API provide basic CRUDs operations for your private locations. See [our documentation](https://docs.escape.tech/docume
  name: Escape Locations API
  slug: escape-locations-api
- description: A Profile is a configuration for the DAST scanning feature. It includes various parameters such as authentication details, environment settings, a schema... Profiles allow you to start scans on an end
  name: Escape Profiles API
  slug: escape-profiles-api
- description: Projects Management The public API provides CRUDs operations to manage projects.
  name: Escape Projects API
  slug: escape-projects-api
- description: Roles Management The public API provides CRUDs operations to manage roles.
  name: Escape Roles API
  slug: escape-roles-api
- description: 'A Scan is a run of the DAST or ASM scanning feature on an profile (DAST/ASM). With the public API, you can trigger scans, track their status, and retrieve their results. See [our documentation](https:'
  name: Escape Scans API
  slug: escape-scans-api
- description: Organization Statistics High-level organization security posture statistics.
  name: Escape Statistics API
  slug: escape-statistics-api
- description: Manage tags. The public API provides basic CRUDs operations to manage tags.
  name: Escape Tags API
  slug: escape-tags-api
- description: Upload helper for Escape Platform. The public API provides endpoints to upload files to the platform.
  name: Escape Upload API
  slug: escape-upload-api
- description: Users Management The public API provides CRUDs operations to manage users.
  name: Escape Users API
  slug: escape-users-api
- description: Workflows Management The public API provides CRUDs operations to manage workflows.
  name: Escape Workflows API
  slug: escape-workflows-api
artifact_total: 48
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Escape Public Asm API
  slug: open-escape-asm-api
- collection_type: open
  name: Escape Public Asm Assets API
  slug: open-escape-assets-api
- collection_type: open
  name: Escape Public Asm Audit API
  slug: open-escape-audit-api
- collection_type: open
  name: Escape Public Asm Beta API
  slug: open-escape-beta-api
- collection_type: open
  name: Escape Public Asm CustomRules API
  slug: open-escape-customrules-api
- collection_type: open
  name: Escape Public Asm Emails API
  slug: open-escape-emails-api
- collection_type: open
  name: Escape Public Asm Events API
  slug: open-escape-events-api
- collection_type: open
  name: Escape Public Asm Integrations API
  slug: open-escape-integrations-api
- collection_type: open
  name: Escape Public Asm Issues API
  slug: open-escape-issues-api
- collection_type: open
  name: Escape Public Asm Jobs API
  slug: open-escape-jobs-api
- collection_type: open
  name: Escape Public Asm Locations API
  slug: open-escape-locations-api
- collection_type: open
  name: Escape Public Asm Profiles API
  slug: open-escape-profiles-api
- collection_type: open
  name: Escape Public Asm Projects API
  slug: open-escape-projects-api
- collection_type: open
  name: Escape Public Asm Roles API
  slug: open-escape-roles-api
- collection_type: open
  name: Escape Public Asm Scans API
  slug: open-escape-scans-api
- collection_type: open
  name: Escape Public Asm Statistics API
  slug: open-escape-statistics-api
- collection_type: open
  name: Escape Public Asm Tags API
  slug: open-escape-tags-api
- collection_type: open
  name: Escape Public Asm Upload API
  slug: open-escape-upload-api
- collection_type: open
  name: Escape Public Asm Users API
  slug: open-escape-users-api
- collection_type: open
  name: Escape Public Asm Workflows API
  slug: open-escape-workflows-api
- collection_type: open
  name: Escape Public API
  slug: open-escape
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/escape-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/escape-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/escape-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/escape-technologies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/escapetech
- group: docs
  title: ''
  type: Documentation
  url: https://docs.escape.tech/
- group: company
  title: ''
  type: Blog
  url: https://escape.tech/blog/
- group: other
  title: ''
  type: CaseStudies
  url: https://escape.tech/blog/tag/case-study/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://escape.tech/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://escape.tech/terms
- group: company
  title: ''
  type: Website
  url: https://escape.tech/
created: '2025-01-08'
description: Escape was founded in 2020 after one of our co-founders experienced a cyberattack and saw firsthand how vulnerable exposed APIs can be. Driven by a belief in the power of AI to transform cybersecurity, we built a platform that emulates hacker behavior to identify vulnerabilities before they can be exploited. Escape is a DAST (Dynamic Application Security Testing) platform that helps you document all your APIs, detect complex business logic flaws across modern applications like APIs, SPAs, and Microservices, and seamlessly integrate security into your CI/CD pipeline.
finops:
- name: Escape Finops
  service_category: API
  slug: escape-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/escape.png
layout: provider
modified: '2026-05-19'
name: Escape
nav: Providers
network: true
overview: 'Escape publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Asm API, Assets API, Audit API, and 17 more. Tagged areas include Platform and Security.


  Escape''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Escape Plans Pricing
  plan_count: 3
  slug: escape-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Escape Rate Limits
  slug: escape-rate-limits
score:
  band: thin
  composite: 35.0
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 60.0
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/escape/refs/heads/main/screenshots/escape-2026-06-20T180822.png
security:
- kind: authentication
  name: Escape Authentication
  slug: escape-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Escape Domain Security
  slug: escape-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: escape
tags:
- Platform
- Security
website: https://escape.tech/
---
