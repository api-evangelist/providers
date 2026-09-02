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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orsobio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orsobio.com/
- group: company
  title: ''
  type: About
  url: https://orsobio.com/about/
- group: other
  title: ''
  type: Science
  url: https://orsobio.com/science/
- group: other
  title: ''
  type: Pipeline
  url: https://orsobio.com/our-pipeline/
- group: other
  title: ''
  type: Team
  url: https://orsobio.com/team/
- group: company
  title: ''
  type: News
  url: https://orsobio.com/news/
- group: company
  title: ''
  type: Blog
  url: https://orsobio.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://orsobio.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orsobio.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orsobio/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/OrsoBio
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/orsobio/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/orsobio_stock/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/orsobio-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orsobio-llms.txt
coverage:
  checked: '2026-08-04'
  detail: OrsoBio is a clinical-stage biopharmaceutical company with no developer program — no api., developer., docs., portal. or status. host resolves for orsobio.com, no orsobio GitHub organisation exists, and every spec path and /.well-known/ document on the corporate site is answered by a SiteGround CAPTCHA interstitial that resolves to the site's WordPress 404 page, leaving only the CMS routes at /wp-json/ that the site's own robots.txt disallows.
  evidence:
  - status: 202
    url: https://orsobio.com/openapi.json
  - status: 202
    url: https://orsobio.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/orsobio
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: 'OrsoBio is a privately held, clinical-stage biopharmaceutical company founded in 2021 and headquartered in Palo Alto, California, developing first-in-class oral therapies that restore energy homeostasis in patients living with severe metabolic disorders — obesity, type 2 diabetes, severe dyslipidemias, lipodystrophies and MASH. The name is drawn from the metabolic adaptability of bears ("orso" in Italian). Its pipeline is led by three mitochondrial protonophores — TLC-6740, TLC-1180 and TLC-1235 — intended to increase energy expenditure and improve metabolic and cardiovascular health, alongside an LXR inverse agonist (TLC-2716) for severe hypertriglyceridemia and MASH, an ACC2 inhibitor (TLC-3595) for insulin sensitivity in type 2 diabetes, and an ACMSD inhibitor to augment NAD+ biosynthesis in metabolic and inflammatory liver and kidney disorders. The company closed an oversubscribed $67 million Series B in September 2024, co-led by Ascenta Capital and Woodline Partners with
  participation from Samsara BioCapital, Enavate Sciences and Longitude Capital. OrsoBio publishes a corporate site covering its science, pipeline, team, board, publications, events and press releases, but runs no developer program: no API documentation, no SDKs, no developer portal, no GitHub organisation and no machine-readable API contract of any kind. The only machine-readable surface on orsobio.com is the site''s own WordPress CMS route index, which the site''s robots.txt explicitly disallows at /wp-json/ and which is therefore not harvested or catalogued here.'
image: https://orsobio.com/wp-content/uploads/2022/10/orso-bio.png
layout: provider
modified: '2026-08-04'
name: OrsoBio
nav: Providers
network: true
overview: 'OrsoBio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Metabolic Disease.


  OrsoBio''s developer surface includes product news, engineering blog, and 14 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orsobio/refs/heads/main/screenshots/orsobio-2026-08-07T190952.png
security:
- kind: domain-security
  name: Orsobio Domain Security
  slug: orsobio-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: orsobio
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Metabolic Disease
- Obesity
- Clinical Trials
- Drug Development
- Healthcare
website: https://orsobio.com/
---
