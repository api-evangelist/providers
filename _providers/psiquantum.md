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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/psiquantum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.psiquantum.com
- group: company
  title: ''
  type: About
  url: https://www.psiquantum.com/about
- group: other
  title: ''
  type: Technology
  url: https://www.psiquantum.com/technology
- group: other
  title: ''
  type: Research
  url: https://www.psiquantum.com/research
- group: other
  title: ''
  type: Applications
  url: https://www.psiquantum.com/applications
- group: other
  title: ''
  type: Software
  url: https://www.psiquantum.com/psiquantum-software
- group: other
  title: ''
  type: CircuitDesigner
  url: https://circuits.psiquantum.com
- group: other
  title: ''
  type: Bartiq
  url: https://github.com/PsiQ/bartiq
- group: docs
  title: ''
  type: BartiqDocs
  url: https://psiq.github.io/bartiq/
- group: other
  title: ''
  type: QREF
  url: https://github.com/PsiQ/qref
- group: docs
  title: ''
  type: QREFDocs
  url: https://psiq.github.io/qref/
- group: other
  title: ''
  type: CircuitHub
  url: https://github.com/PsiQ/circuit-hub
- group: build
  title: ''
  type: GitHub
  url: https://github.com/PsiQ
- group: company
  title: ''
  type: News
  url: https://www.psiquantum.com/news
- group: company
  title: ''
  type: PressMaterials
  url: https://www.psiquantum.com/press-materials
- group: company
  title: ''
  type: Careers
  url: https://www.psiquantum.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.psiquantum.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/psiquantum
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/PsiQuantum
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@psiquantum
created: '2026-05-24'
description: 'PsiQuantum is a Palo Alto, California photonic quantum computing company founded in 2016 by Jeremy O''Brien, Terry Rudolph, Pete Shadbolt, and Mark Thompson, building utility-scale, fault-tolerant quantum computers based on single-photon qubits at telecom wavelength. Its Omega chipset — a silicon photonic system integrating on-chip single-photon sources, superconducting nanowire single-photon detectors, barium-titanate optical switches, and low-loss fiber couplers — is manufactured on 300mm wafers at GlobalFoundries'' flagship fab in Malta, NY, leveraging mature semiconductor processes rather than exotic cryogenic fabrication. The company is constructing two utility- scale, million-qubit, fault-tolerant quantum computing sites: one at Moreton Bay, Queensland, Australia (in partnership with the Australian and Queensland governments) and one at the Illinois Quantum and Microelectronics Park in Chicago, Illinois (with additional R&D at PsiLabs in Daresbury, UK and assembly at
  PsiFactory in Milpitas, CA). PsiQuantum exposes a developer surface aimed at fault-tolerant quantum algorithm researchers: Construct, an enterprise platform for FTQC algorithm development, resource analysis, and training; Circuit Designer, a free web tool for prototyping and visualizing fault-tolerant quantum circuits; Circuit Hub, a shared library of `.circuit` files; and two open-source Python projects on GitHub — Bartiq, a symbolic quantum resource estimator that compiles subroutine-level costs to global T-gate, Toffoli, qubit, and circuit-volume estimates, and QREF, an open JSON-Schema-based format for representing quantum algorithms as hierarchical DAGs with a Pydantic validation library and a `qref-render` visualization tool. NVIDIA''s CUDA-Q is integrated into Construct for accelerated simulation. PsiQuantum does not currently publish a commercial cloud-access REST API, OpenAPI specification, or a general-purpose quantum-execution SDK comparable to those of gate-model quantum cloud
  providers — its public developer artifacts are confined to FTQC resource-estimation tooling and algorithm-design surfaces — and there is no public pricing or self-serve tier for the underlying quantum hardware.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/psiquantum.png
layout: provider
modified: '2026-05-24'
name: PsiQuantum
nav: Providers
network: true
overview: 'PsiQuantum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Quantum Computing, Photonic Quantum Computing, Fault-Tolerant Quantum Computing, FTQC, and Single Photon Qubits.


  PsiQuantum''s developer surface includes GitHub presence, product news, YouTube channel, and 18 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 2
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 5.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/psiquantum/refs/heads/main/screenshots/psiquantum-2026-06-20T192235.png
security:
- kind: domain-security
  name: Psiquantum Domain Security
  slug: psiquantum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: psiquantum
tags:
- Quantum Computing
- Photonic Quantum Computing
- Fault-Tolerant Quantum Computing
- FTQC
- Single Photon Qubits
- Silicon Photonics
- Quantum Resource Estimation
- Quantum Algorithms
- Quantum Software
- Omega Chipset
- Construct
- Circuit Designer
- Bartiq
- QREF
- Semiconductors
- Hardware
website: https://www.psiquantum.com
---
