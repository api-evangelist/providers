---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Advance workflow instances that are paused on an intermediate event.
  name: Liberate Innovations Events API
  slug: liberate-innovations-events-api
- description: Start workflow orchestrations and pass context data into them.
  name: Liberate Innovations Workflows API
  slug: liberate-innovations-workflows-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Liberate Orchestration Platform Events API
  slug: open-liberate-innovations-events-api
- collection_type: open
  name: Liberate Orchestration Platform Events Workflows API
  slug: open-liberate-innovations-workflows-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/liberate-innovations-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/liberate-innovations-orchestration-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liberate-innovations-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.liberateinc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.liberateinc.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.liberateinc.com/docs/calling-a-workflow
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.liberateinc.com/docs/overview
- group: company
  title: ''
  type: Website
  url: https://www.liberateinc.com/
- group: company
  title: ''
  type: Blog
  url: https://www.liberateinc.com/blog
- group: company
  title: ''
  type: News
  url: https://www.liberateinc.com/news
- group: other
  title: ''
  type: Glossary
  url: https://www.liberateinc.com/glossary
- group: other
  title: ''
  type: Resources
  url: https://www.liberateinc.com/resources
- group: company
  title: ''
  type: Careers
  url: https://www.liberateinc.com/careers
- group: company
  title: ''
  type: About
  url: https://www.liberateinc.com/about
- group: start
  title: ''
  type: SignUp
  url: https://www.liberateinc.com/request-demo
- group: start
  title: ''
  type: Login
  url: https://app.liberateinc.com/login
- group: operate
  title: ''
  type: Support
  url: https://signup.liberateinc.com/contact-us
- group: other
  title: ''
  type: Discussions
  url: https://docs.liberateinc.com/discuss
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.liberateinc.com/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.liberateinc.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liberateinc.com/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: security/liberate-innovations-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/liberateinc.com/trust/a3f4px3jh3gd2prixhl6
- group: auth
  title: ''
  type: SecurityOverview
  url: https://www.liberateinc.com/security
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liberate-innovations-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/liberate-inc/
created: '2026-07-17'
description: Liberate Innovations, Inc. (trading as Liberate) is a Palo Alto, California company building insurance-native AI agents for sales, servicing, and claims. Its voice, email, and SMS AI resolves customer inquiries end to end — verifying identity, gathering loss details, and filing a claim without a human rep — and writes the results straight into the carrier's or agency's core systems. Underneath the customer-facing agents sits the Liberate Orchestration Platform, a visual workflow engine where developers compose modular workflows from connections, events, tasks, and decision tables, with JSONata transformations, release management across QA and production environments, and correlation-level session reporting. The platform is driven over a small documented HTTP API that starts workflows by slug and advances paused instances with intermediate events. Liberate integrates with Guidewire, Duck Creek, Salesforce, Vertafore, Applied, EZLynx, Insuresoft, TurboRater, Verisk, CCC, CoreLogic,
  Snapsheet, and Microsoft Outlook.
image: https://cdn.prod.website-files.com/69d93976ca90059d5696cd0b/69d93976ca90059d5696cef7_Webclip.png
layout: provider
mcp_servers:
- description: Liberate publishes no official hosted or remote Model Context Protocol server. No MCP endpoint, npm/PyPI MCP package, registry listing, or mcp.json manifest was found on any Liberate host or in the pu
  name: Liberate Orchestration Platform MCP candidate
  slug: liberate-orchestration-platform-mcp-candidate
modified: '2026-07-19'
name: Liberate Innovations
nav: Providers
network: true
overview: 'Liberate Innovations publishes 2 APIs on the [APIs.io](https://apis.io/) network: Events API and Workflows API. Tagged areas include Company, Insurance, Insurtech, Artificial Intelligence, and Voice AI.


  Liberate Innovations'' developer surface includes documentation, API reference, getting-started guide, engineering blog, product news, signup flow, support, and 20 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 14.1
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 35.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liberate-innovations/refs/heads/main/screenshots/liberate-innovations-2026-07-25T225018.png
security:
- kind: authentication
  name: Liberate Innovations Authentication
  slug: liberate-innovations-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Liberate Innovations Domain Security
  slug: liberate-innovations-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Liberate Innovations Trust Center
  slug: liberate-innovations-trust-center
  summary_line: SOC 2, HIPAA, PCI DSS, GDPR, CCPA, ISO 27001, FedRAMP
slug: liberate-innovations
tags:
- Company
- Insurance
- Insurtech
- Artificial Intelligence
- Voice AI
- Conversational AI
- Workflow Orchestration
- Claims Automation
- Integration
- Contact Center
website: https://www.liberateinc.com/
---
