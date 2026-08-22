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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 58
  human_in_the_loop: 0
  name: Labayh Agentic Access
  operation_count: 102
  slug: labayh-agentic-access
  summary_line: 102 operations · 58 acting
api_count: 7
apis:
- description: Licensed psychologists, psychiatrists and family counsellors listed on Labayh, and the specialty taxonomy used to classify them.
  name: Labayh Consultants API
  slug: labayh-consultants-api
- description: Blog articles, pages, media, taxonomy terms, comments and author profiles.
  name: Labayh Content API
  slug: labayh-content-api
- description: Events published by Labayh and their categories.
  name: Labayh Events API
  slug: labayh-events-api
- description: Discovery, registered types, taxonomies, statuses and cross-content search.
  name: Labayh Meta API
  slug: labayh-meta-api
- description: Structured therapeutic programs and their categories.
  name: Labayh Programs API
  slug: labayh-programs-api
- description: Peer support group offerings and their categories.
  name: Labayh Support Groups API
  slug: labayh-support-groups-api
- description: Live and recorded webinar sessions and their categories.
  name: Labayh Webinars API
  slug: labayh-webinars-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Labayh Content Consultants API
  slug: open-labayh-consultants-api
- collection_type: open
  name: Labayh Consultants Content API
  slug: open-labayh-content-api
- collection_type: open
  name: Labayh Content Consultants Events API
  slug: open-labayh-events-api
- collection_type: open
  name: Labayh Content Consultants Meta API
  slug: open-labayh-meta-api
- collection_type: open
  name: Labayh Content Consultants Programs API
  slug: open-labayh-programs-api
- collection_type: open
  name: Labayh Content Consultants Support Groups API
  slug: open-labayh-support-groups-api
- collection_type: open
  name: Labayh Content Consultants Webinars API
  slug: open-labayh-webinars-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/labayh-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://labayh.net
- group: operate
  title: ''
  type: Support
  url: https://labayh.net/en/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://labayh.net/en/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://labayh.net/en/feed/
- group: start
  title: ''
  type: Login
  url: https://client.labayh.net/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://labayh.net/en/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://labayh.net/en/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.labayh.net/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/labayh-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/labayh-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/labayh-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/labayh-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/labayh-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/labayh-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/labayh-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/labayh-robots.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/labayh-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/labayh-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/labayh-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/labayh-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/labayh-find-consultant.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/labayh-browse-programs.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/labayh-search-content.md
created: '2026-07-17'
description: Labayh (لبيه) is a Saudi Arabian digital mental-health platform delivering online psychological, psychiatric and family counselling to the Arabic-speaking Gulf market. Patients book scheduled or instant video and audio sessions with more than 1,000 licensed specialists, and can also enrol in structured therapeutic programs for depression, anxiety, OCD and social phobia, join peer support groups, take psychological assessments, track mood daily, and watch live and recorded webinars. The company reports over 70 million minutes of consultation delivered. Alongside the consumer app it runs Labayh Business, a corporate employee-wellbeing arm, and Labayh Academy, a training platform for practitioners. Labayh is backed by 500 Global. It operates no developer program and publishes no OpenAPI, SDKs or developer portal; the API catalogued here is the anonymously readable WordPress REST surface behind labayh.net, whose OpenAPI description API Evangelist derived from the server's own discovery
  document.
image: https://labayh.net/wp-content/themes/labayh/assets/images/logo/labayh-logo.svg
json_schemas:
- name: consultant_categories
  property_count: 9
  slug: labayh-consultant-categories
- name: consultant
  property_count: 23
  slug: labayh-consultant
- name: program
  property_count: 23
  slug: labayh-program
- name: recorded_webinar
  property_count: 23
  slug: labayh-recorded-webinar
- name: support_group
  property_count: 23
  slug: labayh-support-group
layout: provider
mcp_servers:
- description: ''
  name: labayh-mcp.yml
  slug: labayh-mcpyml
modified: '2026-07-19'
name: Labayh
nav: Providers
network: true
overview: 'Labayh publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Consultants API, Content API, Events API, and 4 more. Tagged areas include Company, Mental Health, Healthcare, Telehealth, and Therapy.


  Labayh''s developer surface includes support, engineering blog, authentication, and 21 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 40.6
  delta: 2.4
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 16.7
    contract_quality: 67.3
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 15.8
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/labayh/refs/heads/main/screenshots/labayh-2026-07-25T224413.png
security:
- kind: authentication
  name: Labayh Authentication
  slug: labayh-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Labayh Domain Security
  slug: labayh-domain-security
  summary_line: TLSv1.3 · DMARC
slug: labayh
tags:
- Company
- Mental Health
- Healthcare
- Telehealth
- Therapy
- Wellbeing
- Content
- Saudi Arabia
- Middle East
- Arabic
website: https://labayh.net
---
