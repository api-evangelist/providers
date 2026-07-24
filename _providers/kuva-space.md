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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kuva-space-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kuvaspace.com
- group: other
  title: ''
  type: HomeEnglish
  url: https://kuvaspace.com/en
- group: other
  title: ''
  type: Company
  url: https://kuvaspace.com/en/company
- group: other
  title: ''
  type: Technology
  url: https://kuvaspace.com/en/technology
- group: other
  title: ''
  type: Satellites
  url: https://kuvaspace.com/en/technology/satellites
- group: design
  title: ''
  type: HyperspectralImaging
  url: https://kuvaspace.com/en/technology/hyperspectral-imaging
- group: other
  title: ''
  type: KuvaSense
  url: https://kuvaspace.com/en/kuva-sense
- group: other
  title: ''
  type: Agriculture
  url: https://kuvaspace.com/en/solutions/agriculture
- group: other
  title: ''
  type: Aquaculture
  url: https://kuvaspace.com/en/solutions/aquaculture
- group: other
  title: ''
  type: EnvironmentAndCarbon
  url: https://kuvaspace.com/en/solutions/environment-and-carbon
- group: auth
  title: ''
  type: SafetyAndSecurity
  url: https://kuvaspace.com/en/solutions/safety-and-security
- group: other
  title: ''
  type: EarlyAdopterProgram
  url: https://kuvaspace.com/en/early-adopter-program
- group: other
  title: ''
  type: Resources
  url: https://kuvaspace.com/en/resources
- group: company
  title: ''
  type: Newsroom
  url: https://kuvaspace.com/en/resources
- group: company
  title: ''
  type: Careers
  url: https://kuvaspace.com/en/careers
- group: operate
  title: ''
  type: Contact
  url: https://kuvaspace.com/en/contact
- group: build
  title: ''
  type: GitHub
  url: https://github.com/KuvaSpace
- group: build
  title: ''
  type: GitHubDataProcessing
  url: https://github.com/KuvaSpace/kuva-data-processing
- group: other
  title: ''
  type: PyPIReader
  url: https://pypi.org/project/kuva-reader/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kuva-space
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@kuvaspace
- group: other
  title: ''
  type: ESAInCubedHyperfield
  url: https://incubed.esa.int/portfolio/hyperfield/
- group: other
  title: ''
  type: AaltoUniversityProfile
  url: https://www.aalto.fi/en/innovation-portfolio/kuva-space
created: '2026-05-24'
description: Kuva Space is a Finnish space-data company headquartered in Espoo that operates a fleet of hyperspectral Earth observation microsatellites and delivers AI-driven planetary intelligence through its Kuva Sense platform. Founded in 2016 (originally as Reaktor Space Lab) by Tuomas Tikka and Janne Kuhno in collaboration with Reaktor, the company designs, builds, and operates its own 6U CubeSat-class spacecraft carrying a patented in-orbit tunable Fabry-Perot 2D snapshot hyperspectral imager. Its operational Hyperfield-1A (launched August 2024 on SpaceX Falcon 9 from Vandenberg) and Hyperfield-1B (launched June 2025) cover the 475–950 nm VNIR range with up to 160 tunable spectral bands at 25 m spatial resolution and a 50 km swath from a 500 km polar sun-synchronous orbit. The larger 70 kg Hyperfield-2 microsatellite, scheduled for H2 2026, expands coverage to 450–1,650 nm at 15 m resolution with an additional 3.6 m GSD RGB camera. By 2030 Kuva Space plans to grow the constellation
  to roughly 100 satellites to enable sub-daily revisit anywhere on Earth. Onboard AI handles cloud filtering, spectral band alignment, and compression so that downlinked products feed directly into Kuva Sense, where automated analytics generate insights-as-a-service for agriculture (crop identification, yield forecasting, harvest timing), aquaculture (water quality, algal bloom detection, biomass), environment and carbon (sequestration monitoring, deforestation, pollution tracking), and safety and security (vessel detection and tracking, illegal activity warning, rapid change detection). Kuva Space is part of the European Space Agency InCubed-co-funded HYPERFIELD program, was awarded a €1.8M ESA Civil Security from Space contract within the SMART-CONNECT consortium to demonstrate rapid hyperspectral insights for crisis response, and in 2026 signed a Letter of Intent with SSC Space to strengthen Nordic space capabilities. The commercial model is subscription-based insights-as-a-service rather
  than pay-per-pixel imagery sales, with current access offered through the Kuva Sense Early Adopter Program; the company markets "robust APIs and customizable data formats" for system integration but does not currently publish open public API reference documentation, an OpenAPI specification, or a self-service developer portal. The only public engineering surface is the open-source kuva-data-processing Python toolkit (kuva-metadata, kuva-reader, kuva-geometry) on GitHub and PyPI, which reads Kuva GeoTIFF-based L0/L1AB/L1C/L2A data products and their metadata sidecars.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kuva-space.png
layout: provider
modified: '2026-05-24'
name: Kuva Space
nav: Providers
network: true
overview: 'Kuva Space is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Earth Observation, Hyperspectral Imaging, Satellite Imagery, Remote Sensing, and Microsatellites.


  Kuva Space''s developer surface includes GitHub presence, YouTube channel, and 22 more developer resources.'
random_paper: 39
score:
  band: minimal
  composite: 7.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 7.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kuva-space/refs/heads/main/screenshots/kuva-space-2026-06-20T184221.png
security:
- kind: domain-security
  name: Kuva Space Domain Security
  slug: kuva-space-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kuva-space
tags:
- Earth Observation
- Hyperspectral Imaging
- Satellite Imagery
- Remote Sensing
- Microsatellites
- CubeSat
- Space
- Geospatial
- Planetary Intelligence
- Agriculture
- Aquaculture
- Environment
- Carbon Monitoring
- Deforestation
- Maritime Domain Awareness
- Safety And Security
- Crisis Response
- Climate
- AI
- Insights As A Service
- Finland
- Nordic Space
- ESA InCubed
- Hyperfield
- Kuva Sense
website: https://kuvaspace.com
---
