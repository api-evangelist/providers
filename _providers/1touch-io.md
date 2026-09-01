---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.1touch.io/
- group: company
  title: ''
  type: Blog
  url: https://www.1touch.io/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.1touch.io/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.1touch.io/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.1touch.io/vulnerability-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/1touch-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/1touch-io-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.1touch.io/resources/trust-and-security-center
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1touch-io-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/1touch-io-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1touch-io-llms.txt
coverage:
  checked: '2026-08-05'
  detail: The only product documentation 1touch.io publishes sits at help.1touch.io/docs/ as a MadCap Flare output whose content files all redirect to a MadCap Central "Secure Login" page (a random control path returns the identical login body), and the API host api.1touch.io resolves to 18.156.148.123 but times out on both 443 and 80 from the public internet.
  evidence:
  - status: 200
    url: https://help.1touch.io/docs/Data/Toc.js
  - status: 200
    url: https://help.1touch.io/robots.txt
  - status: 404
    url: https://www.1touch.io/.well-known/agent-card.json
  - status: 404
    url: https://www.1touch.io/openapi.json
  - status: 404
    url: https://www.1touch.io/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-05'
description: '1touch.io is an enterprise data-security and data-intelligence vendor whose Kontxtual platform (previously shipped as Inventa) performs automated, near real-time discovery, classification, mapping and cataloging of sensitive data across cloud, on-premises, SaaS and IBM z/OS mainframe environments. The platform combines passive network analysis, ML/NLP classification and an LLM-driven contextual graph to deliver enterprise DSPM, attribute-based access control, access intelligence, DLP for streaming data, mainframe security posture management, cryptographic discovery and AI security. The technology is also OEM-distributed by IBM as Guardium Discover and Classify. Everpure (formerly Pure Storage, NYSE: PSTG) completed its acquisition of 1touch.io on 2026-05-11. Product documentation is published to a MadCap Central portal that requires a customer login, and no public developer portal, API reference or machine-readable specification is available.'
image: https://cdn.prod.website-files.com/66c7d1456cadd6a7c0d9b336/6a04f52a14465da1c82c33e8_68e91c7569e51953a3b740fe_a942d4_f57651eebc6c4161a04456c4fd56709c_mv2.png
layout: provider
modified: '2026-08-05'
name: 1touch.io
nav: Providers
network: true
overview: '1touch.io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Security, Data Discovery, Data Classification, and DSPM.


  1touch.io''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 16.0
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/1touch-io/refs/heads/main/screenshots/1touch-io-2026-08-07T160653.png
security:
- kind: domain-security
  name: 1Touch Io Domain Security
  slug: 1touch-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 1Touch Io Vulnerability Disclosure
  slug: 1touch-io-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: 1Touch Io Trust Center
  slug: 1touch-io-trust-center
  summary_line: SOC 2 Type 2, ISO 27001
slug: 1touch-io
tags:
- Company
- Data Security
- Data Discovery
- Data Classification
- DSPM
- Data Governance
- Privacy
- Compliance
- Mainframe
- Access Control
- AI Security
website: https://www.1touch.io/
---
