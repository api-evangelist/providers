---
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phononic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://phononic.com/
- group: operate
  title: ''
  type: Support
  url: https://phononic.com/customer-support/
- group: company
  title: ''
  type: Blog
  url: https://phononic.com/intelligence-hub/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://phononic.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://phononic.com/sales-terms-and-conditions/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/phononic-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/phononic-conformance.yml
coverage:
  checked: '2026-08-05'
  detail: Phononic markets "API-accessible control firmware" with "Redfish-compatible open-source interfaces" on its Thermal Kit product page, but publishes no reference, no spec and no developer portal anywhere on phononic.com - the page ends at a customer-support contact form, and the one API host that does exist, api.phononic.com, answers every path with a Cloudflare managed challenge.
  evidence:
  - status: 200
    url: https://phononic.com/predictive-cooling-software-firmware-redfish-compatible/
  - status: 404
    url: https://phononic.com/developers
  - status: 404
    url: https://phononic.com/redfish/v1
  - status: 403
    url: https://api.phononic.com/openapi.json
  - status: 200
    url: https://phononic.com/llms.txt
  reason: sales-gate
  state: gated
created: '2026-08-05'
description: Phononic is a Durham, North Carolina solid-state cooling company founded by CEO Tony Atti that replaces compressor-based refrigeration with semiconductor thermoelectric devices. Its products cool optical and fiber transceivers, co-packaged optics, GPU high-bandwidth memory, LiDAR sensors, medical and vaccine cold chain, grocery retail merchandising and HVAC. The current focus is AI data centers, where the Thermal Kit and Thermal Fabric combine thermoelectric cooling chips with embedded control firmware that the company markets as API-accessible and Redfish-compatible, delivering millisecond thermal response plus real-time telemetry and analytics. Phononic publishes no public developer portal, API reference or machine-readable specification; technical access runs through sales and customer support.
image: https://phononic.com/wp-content/uploads/cropped-favicon-270x270.png
layout: provider
modified: '2026-08-05'
name: Phononic
nav: Providers
network: true
overview: 'Phononic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Hardware, Cooling, and Thermal Management.


  Phononic''s developer surface includes support, engineering blog, and 6 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 13.6
  delta: 0.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 12.8
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Phononic Domain Security
  slug: phononic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: phononic
tags:
- Company
- Semiconductors
- Hardware
- Cooling
- Thermal Management
- Data Center
- Artificial Intelligence
- Optoelectronics
- Sustainability
- Manufacturing
website: https://phononic.com/
---
