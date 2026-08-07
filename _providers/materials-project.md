---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Materials Project Agentic Access
  operation_count: 41
  slug: materials-project-agentic-access
  summary_line: 41 operations · 1 acting
api_count: 29
apis:
- description: The Defect Tasks API from Materials Project — 1 operation(s) for defect tasks.
  name: Materials Project Defect Tasks API
  slug: materials-project-defect-tasks-api
- description: Route providing DOI and bibtex reference information for a material. Note that this data may not be available for all materials in the Materials Project database. See the `DOIDoc` schema for a full li
  name: Materials Project DOIs API
  slug: materials-project-dois-api
- description: Route providing computed data for a legacy molecule such as charge, electron affinity, and ionization energy. The unique identifier for a molecule is its `task_id` (e.g. `mol-45807`). See the `Molecul
  name: Materials Project JCESR Electrolyte Genome API
  slug: materials-project-jcesr-electrolyte-genome-api
- description: The Materials Absorption API from Materials Project — 1 operation(s) for materials absorption.
  name: Materials Project Materials Absorption API
  slug: materials-project-materials-absorption-api
- description: Route for retrevial of information about which hypothetical alloy(s) a given material might belong to, following the methodolgy discussed by [Woods-Robinson, Horton and Persson](https://arxiv.org/pdf/
  name: Materials Project Materials Alloys API
  slug: materials-project-materials-alloys-api
- description: Route for "core" information associated with a given material in the Materials Project database. The unique identifier for a material is its `material_id` (e.g. `mp-149`). Core data in this context re
  name: Materials Project Materials API
  slug: materials-project-materials-api
- description: Route for retrevial of bonding information for a given material.
  name: Materials Project Materials Bonds API
  slug: materials-project-materials-bonds-api
- description: The Materials Chemical Environment API from Materials Project — 1 operation(s) for materials chemical environment.
  name: Materials Project Materials Chemical Environment API
  slug: materials-project-materials-chemical-environment-api
- description: Route providing computed dielectric data for a material following the methodology discussed by [Petousis *et al.*](https://doi.org/10.1038/sdata.2016.134) Note that dielectric data has not been calcul
  name: Materials Project Materials Dielectric API
  slug: materials-project-materials-dielectric-api
- description: Route providing computed elasticity data for a material following the methodology discussed by [de Jong *et al.*](https://doi.org/10.1038/sdata.2015.9) Note that elasticity data has not been calculate
  name: Materials Project Materials Elasticity API
  slug: materials-project-materials-elasticity-api
- description: Route providing computed electrode data for a material following the methodology discussed by [Shen *et al.*](https://doi.org/10.1038/s41524-020-00422-3) Note that electrode data has not been calculat
  name: Materials Project Materials Electrodes API
  slug: materials-project-materials-electrodes-api
- description: Routes providing computed electronic structure related data for a material such as band gap and fermi level. Python objects for line-mode band structures, density of states, and fermi surfaces are als
  name: Materials Project Materials Electronic Structure API
  slug: materials-project-materials-electronic-structure-api
- description: Route providing computed equations of state data for a material following the methodology discussed by [Latimer *et al.*](https://doi.org/10.1038/s41524-018-0091-x) Note that equations of state data h
  name: Materials Project Materials EOS API
  slug: materials-project-materials-eos-api
- description: Route providing computed grain boundary data for a material following the methodology discussed by [Hui *et al.*](https://doi.org/10.1016/j.actamat.2019.12.030) Note that grain boundary data has not b
  name: Materials Project Materials Grain Boundaries API
  slug: materials-project-materials-grain-boundaries-api
- description: Route providing computed magnetic ordering related data for a material following the methodology discussed by [Horton *et al.*](https://doi.org/10.1038/s41524-019-0199-7) Note that magnetic data has n
  name: Materials Project Materials Magnetism API
  slug: materials-project-materials-magnetism-api
- description: Route providing computed oxidation state data for a material following the methodology employed by the [BVAnalyzer](https://pymatgen.org/pymatgen.analysis.bond_valence.html) in Pymatgen. Note that oxi
  name: Materials Project Materials Oxidation States API
  slug: materials-project-materials-oxidation-states-api
- description: '**Under construction** Route providing computed phonon data for a material following the methodology discussed by [Petretto *et al.*](https://doi.org/10.1038/sdata.2018.65) Note that phonon data has n'
  name: Materials Project Materials Phonon API
  slug: materials-project-materials-phonon-api
- description: Route providing computed piezoelectric data for a material following the methodology discussed by [de Jong *et al.*](https://doi.org/10.1038/sdata.2015.53) Note that piezoelectric data has not been ca
  name: Materials Project Materials Piezoelectric API
  slug: materials-project-materials-piezoelectric-api
- description: Route providing provenance data for a material such as whether it is theoretical, its associated ICSD entries, and relevant references in literature. Note that provenance data may not be available for
  name: Materials Project Materials Provenance API
  slug: materials-project-materials-provenance-api
- description: 'Route providing a computed text description for a material following the methodology discussed by [Ganose *et al.*](https://doi.org/10.1557/mrc.2019.94) Note that descriptions may not been calculated '
  name: Materials Project Materials Robocrystallographer API
  slug: materials-project-materials-robocrystallographer-api
- description: Route providing a computed similarity metric between materials following the methodology discussed by Zimmerman *et al.* in [10.3389/fmats.2017.00034](https://doi.org/10.3389/fmats.2017.00034) and [10
  name: Materials Project Materials Similarity API
  slug: materials-project-materials-similarity-api
- description: Route providing computed suggested substrate data for a material following the methodology discussed by [Ding *et al.*](https://doi.org/10.1021/acsami.6b01630) Note that substrate data has not been ca
  name: Materials Project Materials Substrates API
  slug: materials-project-materials-substrates-api
- description: Route providing a large amount of amalgamated data for a material. This is constructed by combining subsets of data from many of the other API endpoints. The summary endpoint is very useful for perfor
  name: Materials Project Materials Summary API
  slug: materials-project-materials-summary-api
- description: Route providing computed surface property data for a material following the methodology discussed by [Tran *et al.*](https://doi.org/10.1038/sdata.2016.80) Note that surface data has not been calculat
  name: Materials Project Materials Surface Properties API
  slug: materials-project-materials-surface-properties-api
- description: Route providing a synthesis recipes for materials extracted from literature following the methodology discussed by [Kononova *et al.*](https://doi.org/10.1038/s41597-019-0224-1) Note that synthesis re
  name: Materials Project Materials Synthesis API
  slug: materials-project-materials-synthesis-api
- description: Route for "core" information associated with a given calculation in the Materials Project database. Multiple calculations can ultimately be associated with a unique material, and are the source of its
  name: Materials Project Materials Tasks API
  slug: materials-project-materials-tasks-api
- description: Route providing computed thermodynamic data for a material such as formation energy and energy above hull. Corrected energy values are also available that employ the schemes discussed by [Jain *et al.
  name: Materials Project Materials Thermo API
  slug: materials-project-materials-thermo-api
- description: Route providing computed x-ray absorption spectroscopy data for a material following the methodology discussed by [Mathew *et al.*](https://doi.org/10.1038/sdata.2018.151) and [Chen *et al.*](https://
  name: Materials Project Materials XAS API
  slug: materials-project-materials-xas-api
- description: Route for a summary of all data calculated on 'core' molecules in the Materials Project molecules database. See the `MoleculeSummaryDoc` schema for a full list of fields returned by this route.
  name: Materials Project Molecules Summary API
  slug: materials-project-molecules-summary-api
artifact_total: 36
collections:
- collection_type: open
  name: Materials Project API
  slug: open-materials-project
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/materials-project-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/materials-project-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/materials-project-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://materialsproject.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.materialsproject.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/materialsproject
- group: start
  title: ''
  type: Signup
  url: https://materialsproject.org/login
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.materialsproject.org/llms.txt
created: '2025-02-06'
description: The Materials Project API provides direct access to the Materials Project database, a large-scale computational materials science database with data on tens of thousands of materials. The API is offered free of charge and supports machine learning, automated analysis, and bulk data downloads.
finops:
- name: Materials Project Finops
  service_category: API
  slug: materials-project-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/materials-project.png
layout: provider
modified: '2026-05-19'
name: Materials Project
nav: Providers
network: true
overview: 'Materials Project publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Defect Tasks API, DOIs API, JCESR Electrolyte Genome API, and 26 more. Tagged areas include Chemistry, Materials Science, Physics, Research, and Scientific Computing.


  Materials Project''s developer surface includes authentication, developer portal, documentation, signup flow, and 4 more developer resources.'
plans:
- name: Materials Project Plans Pricing
  plan_count: 3
  slug: materials-project-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 5
  name: Materials Project Rate Limits
  slug: materials-project-rate-limits
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.2
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 29
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/materials-project/refs/heads/main/screenshots/materials-project-2026-06-20T185036.png
security:
- kind: authentication
  name: Materials Project Authentication
  slug: materials-project-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Materials Project Domain Security
  slug: materials-project-domain-security
  summary_line: TLSv1.3
slug: materials-project
tags:
- Chemistry
- Materials Science
- Physics
- Research
- Scientific Computing
website: https://materialsproject.org/
---
