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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 4
apis:
- description: 'REST API for the Diligent One Platform (formerly HighBond) covering the governance, risk, and compliance surface - organizations, projects, control tests, risks, controls, issues, frameworks, results '
  name: Diligent HighBond API (Diligent One)
  slug: diligent-highbond-api
- description: GraphQL API for Diligent Entities - managing company/legal-entity records, their structure, obligations, and legal characteristics, plus an Entities Reports API. Root-level mutations create, update, a
  name: Diligent Entities API
  slug: diligent-entities-api
- description: Developer interface for the Diligent ESG platform, used to send activity-entry (usage) data into Diligent ESG from internal systems for sustainability and emissions reporting. REST over HTTPS with JSO
  name: Diligent ESG API
  slug: diligent-esg-api
- description: 'REST API built around standard HTTPS requests with JSON responses for the Diligent Workflow product. Reports across Business Areas, Job Owners, Jobs, Tasks, Campaigns, and expiries, plus creating and '
  name: Diligent Workflow API
  slug: diligent-workflow-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/diligent-boards-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/diligent-boards-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/diligent-boards-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/diligent
- group: company
  title: ''
  type: Website
  url: https://www.diligent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.diligent.com/
- group: company
  title: ''
  type: Partners
  url: https://www.diligent.com/company/partners
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.diligent.com/docs/api_terms_of_use
- group: other
  title: ''
  type: BoardManagement
  url: https://www.diligent.com/lp/more-than-a-board-portal
created: '2026-07-05'
description: Diligent Corporation is a governance, risk, and compliance (GRC) software company best known for its board management portal (Diligent Boards / Boardbooks) and the broader Diligent One Platform, which unifies board management, enterprise risk, audit, compliance, entity management, and ESG. The board portal itself is a security-hardened product with no public developer API - it is integrated through SSO (SAML 2.0), SCIM provisioning, and packaged connectors (Okta, Microsoft 365/Teams, Zoom, DocuSign). Diligent does, however, publish a real developer portal at developer.diligent.com covering the GRC side of the platform - the HighBond (Diligent One) REST API for audit/risk/compliance data, a GraphQL Entities API for legal-entity and subsidiary management, an ESG API for activity/usage data, and a Workflow API for jobs, tasks, and campaigns. API access is customer/partner-gated (a HighBond API key or SSO-scoped token is required) and pricing is quote-based via Diligent sales.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/diligent-boards.png
layout: provider
modified: '2026-07-05'
name: Diligent
nav: Providers
network: true
overview: 'Diligent publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Governance, Risk, Compliance, GRC, and Board Management.


  Diligent''s developer surface includes documentation and 8 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 12.8
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/diligent-boards/refs/heads/main/screenshots/diligent-boards-2026-07-25T212042.png
security:
- kind: domain-security
  name: Diligent Boards Domain Security
  slug: diligent-boards-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Diligent Boards Vulnerability Disclosure
  slug: diligent-boards-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Diligent Boards Trust Center
  slug: diligent-boards-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR
slug: diligent-boards
tags:
- Governance
- Risk
- Compliance
- GRC
- Board Management
- Audit
- Entity Management
- ESG
- Enterprise
website: https://www.diligent.com/
---
