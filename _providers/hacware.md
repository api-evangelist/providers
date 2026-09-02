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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 54
  human_in_the_loop: 3
  name: Hacware Agentic Access
  operation_count: 113
  slug: hacware-agentic-access
  summary_line: 113 operations · 54 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: The Admin API from Hacware — 3 operation(s) for admin.
  name: Hacware Admin API
  slug: hacware-admin-api
- description: The Compliance API from Hacware — 7 operation(s) for compliance.
  name: Hacware Compliance API
  slug: hacware-compliance-api
- description: The Compliance-Tenant API from Hacware — 5 operation(s) for compliance-tenant.
  name: Hacware Compliance-Tenant API
  slug: hacware-compliance-tenant-api
- description: The Customer API from Hacware — 6 operation(s) for customer.
  name: Hacware Customer API
  slug: hacware-customer-api
- description: The Email-Tenant API from Hacware — 1 operation(s) for email-tenant.
  name: Hacware Email-Tenant API
  slug: hacware-email-tenant-api
- description: The Group API from Hacware — 12 operation(s) for group.
  name: Hacware Group API
  slug: hacware-group-api
- description: The Multi-Tenant API from Hacware — 5 operation(s) for multi-tenant.
  name: Hacware Multi-Tenant API
  slug: hacware-multi-tenant-api
- description: The Phishing API from Hacware — 17 operation(s) for phishing.
  name: Hacware Phishing API
  slug: hacware-phishing-api
- description: The Report API from Hacware — 16 operation(s) for report.
  name: Hacware Report API
  slug: hacware-report-api
- description: The Training API from Hacware — 28 operation(s) for training.
  name: Hacware Training API
  slug: hacware-training-api
- description: The User API from Hacware — 9 operation(s) for user.
  name: Hacware User API
  slug: hacware-user-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Security Awareness API Documentation Admin API
  slug: open-hacware-admin-api
- collection_type: open
  name: Security Awareness API Documentation Admin Compliance API
  slug: open-hacware-compliance-api
- collection_type: open
  name: Security Awareness API Documentation Admin Compliance-Tenant API
  slug: open-hacware-compliance-tenant-api
- collection_type: open
  name: Security Awareness API Documentation Admin Customer API
  slug: open-hacware-customer-api
- collection_type: open
  name: Security Awareness API Documentation Admin Email-Tenant API
  slug: open-hacware-email-tenant-api
- collection_type: open
  name: Security Awareness API Documentation Admin Group API
  slug: open-hacware-group-api
- collection_type: open
  name: Security Awareness API Documentation Admin Multi-Tenant API
  slug: open-hacware-multi-tenant-api
- collection_type: open
  name: Security Awareness API Documentation Admin Phishing API
  slug: open-hacware-phishing-api
- collection_type: open
  name: Security Awareness API Documentation Admin Report API
  slug: open-hacware-report-api
- collection_type: open
  name: Security Awareness API Documentation Admin Training API
  slug: open-hacware-training-api
- collection_type: open
  name: Security Awareness API Documentation Admin User API
  slug: open-hacware-user-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hacware-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hacware-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hacware-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://hacware.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hacware.com/dev.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.hacware.com/doc/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.hacware.com/doc/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://hacware.com/dev.html#partner-app
- group: commercial
  title: ''
  type: Pricing
  url: https://hacware.com/dev.html
- group: start
  title: ''
  type: SignUp
  url: https://hacware.com/
- group: operate
  title: ''
  type: Support
  url: mailto:hello@hacware.com
- group: company
  title: ''
  type: Blog
  url: https://resources.hacware.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hacware.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hacware.com/privacy.pdf
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hacware-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hacware-domain-security.yml
created: '2026-07-17'
description: 'HacWare is an AI-powered security awareness training and phishing simulation platform that helps organizations reduce human-factor cyber risk. Its RESTful Security Awareness API lets partners and developers embed HacWare into their own products: schedule and manage AI-generated phishing simulations (clickable link, attachment, direct response, and SMS), enroll users in micro-training courses, lesson plans and quizzes, run dark web breach reporting and human-risk assessments, manage users, groups and Microsoft 365 security groups, and operate a multi-tenant partner/customer hierarchy with compliance evidence retrieval. The API is documented with apiDoc and exposes 114 operations across Phishing, Training, Reporting, User, Group, Compliance, and Multi-Tenant surfaces. HacWare is a Techstars portfolio company.'
image: https://hacware.com/img/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Hacware MCP Server
  slug: hacware-mcp-server
modified: '2026-07-19'
name: Hacware
nav: Providers
network: true
overview: 'Hacware publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Compliance API, Compliance-Tenant API, and 8 more. Tagged areas include Company, Security, Cybersecurity, Security Awareness, and Phishing.


  Hacware''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 10 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 52.1
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hacware/refs/heads/main/screenshots/hacware-2026-07-25T220524.png
security:
- kind: authentication
  name: Hacware Authentication
  slug: hacware-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hacware Domain Security
  slug: hacware-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: hacware
tags:
- Company
- Security
- Cybersecurity
- Security Awareness
- Phishing
- Training
- Compliance
- Email Security
- Artificial Intelligence
website: https://hacware.com/
---
