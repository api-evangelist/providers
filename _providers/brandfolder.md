---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Brandfolder Agentic Access
  operation_count: 73
  slug: brandfolder-agentic-access
  summary_line: 73 operations · 38 acting
api_count: 1
apis:
- description: RESTful JSON API providing programmatic access to Brandfolder resources including organizations, brandfolders, collections, sections, assets, attachments, tags, custom fields, labels, invitations, use
  name: Brandfolder API
  slug: brandfolder-api
artifact_total: 12
asyncapis:
- description: ''
  name: Brandfolder Webhooks
  slug: brandfolder-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brandfolder-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brandfolder-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/brandfolder-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brandfolder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brandfolder.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.smartsheet.com/api/brandfolder
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brandfolder
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brandfolder-inc-
- group: company
  title: ''
  type: Blog
  url: https://brandfolder.engineering/
- group: commercial
  title: ''
  type: Pricing
  url: https://brandfolder.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brandfolder.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/Brandfolder
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.smartsheet.com/api/brandfolder
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.smartsheet.com/api/brandfolder/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.smartsheet.com/brandfolder
- group: operate
  title: ''
  type: Community
  url: https://community.smartsheet.com/
- group: start
  title: ''
  type: Login
  url: https://brandfolder.com/signin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.smartsheet.com/legal/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smartsheet.com/legal/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.smartsheet.com/legal/bugbounty
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/brandfolder-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.smartsheet.com/legal/security
- group: design
  title: ''
  type: Conformance
  url: conformance/brandfolder-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/brandfolder-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/brandfolder-packages.yml
- group: design
  title: ''
  type: Components
  url: components/brandfolder-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brandfolder-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brandfolder-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/brandfolder-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brandfolder-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/brandfolder-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brandfolder-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brandfolder-finops.yml
created: 2026-06-13
description: Brandfolder is a digital asset management (DAM) platform and Smartsheet company that provides a RESTful API for managing brand assets, collections, sections, tags, share links, webhooks, and asset distribution permissions. The API enables organizations to push Brandfolder content to other applications, pull data from external sources, and synchronize Brandfolder with other platforms.
finops:
- name: Brandfolder Finops
  service_category: ''
  slug: brandfolder-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brandfolder.png
jsonld:
- class_count: 0
  name: Brandfolder Context
  property_count: 13
  slug: brandfolder-context
layout: provider
mcp_servers:
- description: ''
  name: brandfolder-mcp.yml
  slug: brandfolder-mcpyml
modified: 2026-08-13
name: Brandfolder
nav: Providers
network: true
overview: 'Brandfolder publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Asset Management, DAM, Brand Management, Assets, and Media.


  The Brandfolder catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Brandfolder''s developer surface includes authentication, documentation, engineering blog, pricing, getting-started guide, support, changelog, and 27 more developer resources.'
plans:
- name: Brandfolder Plans Pricing
  plan_count: 2
  slug: brandfolder-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Brandfolder Rate Limits
  slug: brandfolder-rate-limits
score:
  band: strong
  composite: 55.4
  delta: -7.6
  facets:
    access_clarity: 82.9
    commercial_clarity: 82.9
    contract_governance: 16.7
    contract_quality: 69.9
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 63.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/brandfolder/refs/heads/main/screenshots/brandfolder-2026-06-20T173633.png
security:
- kind: authentication
  name: Brandfolder Authentication
  slug: brandfolder-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Brandfolder Domain Security
  slug: brandfolder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Brandfolder Vulnerability Disclosure
  slug: brandfolder-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Brandfolder Trust Center
  slug: brandfolder-trust-center
  summary_line: SOC 2, HIPAA
slug: brandfolder
tags:
- Digital Asset Management
- DAM
- Brand Management
- Assets
- Media
- Collections
- Smartsheet
website: https://brandfolder.com
---
