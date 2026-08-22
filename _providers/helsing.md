---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 8
apis:
- description: 'Altra is Helsing''s reconnaissance-strike software platform. It fuses multi-sensor and multi-drone data feeds to cover wider areas, identify targets, and coordinate strikes. Altra is the AI layer that '
  name: Helsing Altra
  slug: altra
- description: Centaur is Helsing's AI fighter pilot. It can function as an autonomous combat agent on board fighter jets, operate independently or as part of a swarm, and integrate with allied airframes. In 2025 He
  name: Helsing Centaur
  slug: centaur
- description: 'Cirra is Helsing''s electronic-warfare AI for detecting, classifying, and responding to electromagnetic-spectrum threats. It powers Helsing''s contribution to programmes such as the Eurofighter Typhoon '
  name: Helsing Cirra
  slug: cirra
- description: Lura is Helsing's underwater AI. It rapidly processes acoustic data to detect and classify ships and submarines while emitting significantly less noise than conventional sonar.
  name: Helsing Lura
  slug: lura
- description: HF-1 is an AI-enabled loitering-munition strike drone. It uses on-board AI and stored map data to navigate and target without relying on GPS. HF-1 has been used by the Ukrainian government in its defe
  name: Helsing HF-1
  slug: hf-1
- description: HX-2 is Helsing's next-generation AI strike drone. Like HF-1 it operates without GPS and runs on-board target recognition. HX-2 is manufactured at Helsing's factory in southern Germany.
  name: Helsing HX-2
  slug: hx-2
- description: CA-1 Europa is Helsing's autonomous combat aircraft. It flies Centaur as its AI pilot and is targeted for first flight in 2027.
  name: Helsing CA-1 Europa
  slug: ca-1-europa
- description: SG-1 Fathom is Helsing's long-endurance underwater drone, capable of operating submerged for up to 90 days and running Lura's acoustic-processing AI on board.
  name: Helsing SG-1 Fathom
  slug: sg-1-fathom
artifact_total: 32
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helsing-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://helsing.ai
- group: company
  title: ''
  type: Blog
  url: https://helsing.ai/newsroom
- group: company
  title: ''
  type: Careers
  url: https://helsing.ai/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/helsing-ai
- group: operate
  title: ''
  type: Support
  url: https://helsing.ai
- group: company
  title: ''
  type: Investors
  url: ''
- group: other
  title: ''
  type: Notes
  url: ''
created: '2026-05-23'
description: Helsing SE is a Munich-based European defense AI company founded in March 2021 by Torsten Reil, Gundbert Scherf, and Niklas Köhler. Helsing builds AI software and autonomous weapons systems for European and allied militaries — reconnaissance-strike software (Altra), electronic-warfare AI (Cirra), an AI fighter pilot (Centaur), loitering-munition strike drones (HF-1 and HX-2), an autonomous combat aircraft (CA-1 Europa), and underwater autonomy (Lura acoustic processing, SG-1 Fathom long-endurance underwater drones). The company is sales-led and government-restricted; there is no public REST API or developer portal. This profile documents the publicly visible product surfaces and partnerships rather than endpoint shapes. Funding totals roughly €1.37B across four rounds, with a $1.2B Series E at an $18B valuation reportedly being finalized as of May 2026. Daniel Ek's Prima Materia is the largest shareholder. Public partnerships include Saab (Gripen E integration of Centaur, including
  the 2025 Project Beyond combat trial), Airbus, Rheinmetall, the Bundeswehr, and the Eurofighter Typhoon EK programme.
features:
- description: Fuses multi-sensor and multi-drone data to identify targets and coordinate strikes across a wider area.
  name: Altra Reconnaissance-Strike Software
- description: Autonomous combat agent for fighter aircraft, demonstrated in 2025's Project Beyond against a human-piloted Gripen.
  name: Centaur AI Fighter Pilot
- description: AI for detecting, classifying, and responding to electromagnetic-spectrum threats; integrated into the Eurofighter Typhoon EK programme.
  name: Cirra Electronic Warfare AI
- description: Quiet acoustic processing for detection and classification of ships and submarines.
  name: Lura Underwater AI
- description: GPS-independent AI strike drone fielded in Ukraine.
  name: HF-1 Loitering Munition
- description: Next-generation GPS-independent AI strike drone manufactured in southern Germany.
  name: HX-2 Loitering Munition
- description: Helsing's own UCAV platform flying Centaur, first flight targeted for 2027.
  name: CA-1 Europa Autonomous Combat Aircraft
- description: Long-endurance underwater drone capable of 90-day submerged operations running Lura on board.
  name: SG-1 Fathom Underwater Drone
- description: European-headquartered AI defense supplier serving Germany, France, the UK, Estonia, Ukraine, and allied militaries.
  name: Sovereign European Defense AI
finops:
- name: Helsing Finops
  service_category: API
  slug: helsing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/helsing.png
integrations:
- description: Centaur integrated into the Saab Gripen E; 2025 Project Beyond combat trial.
  name: Saab
- description: Helsing's AI (including Cirra) integrated into the Eurofighter Typhoon EK electronic-warfare variant.
  name: Eurofighter Typhoon EK
- description: Strategic partnership for European defense aerospace programmes.
  name: Airbus
- description: Industrial partnership inside Germany's defense base.
  name: Rheinmetall
- description: Customer relationship with the German armed forces.
  name: Bundeswehr
- description: Operational user of HF-1 strike drones in the defence against Russia's invasion.
  name: Government of Ukraine
layout: provider
modified: '2026-05-23'
name: Helsing
nav: Providers
network: true
overview: 'Helsing publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Defense AI, European Defense, Autonomy, Loitering Munitions, and Underwater Autonomy.


  Helsing''s developer surface includes developer portal, engineering blog, support, and 3 more developer resources.'
plans:
- name: Helsing Plans Pricing
  plan_count: 1
  slug: helsing-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Helsing Rate Limits
  slug: helsing-rate-limits
score:
  band: emerging
  composite: 17.6
  delta: -0.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Helsing Domain Security
  slug: helsing-domain-security
  summary_line: TLSv1.3 · DMARC
slug: helsing
tags:
- Defense AI
- European Defense
- Autonomy
- Loitering Munitions
- Underwater Autonomy
- Electronic Warfare
- AI Fighter Pilot
- Sovereign AI
use_cases:
- description: Provide Centaur AI fighter-pilot capability for European and allied air forces, including Saab Gripen and Eurofighter programmes.
  name: Sovereign European Air Combat AI
- description: Deliver HF-1 and HX-2 GPS-independent strike drones to allied militaries and Ukraine.
  name: Loitering Munition Strike
- description: Provide Cirra EW AI inside platforms such as the Eurofighter Typhoon EK.
  name: Electronic Warfare
- description: Run Lura acoustic processing on SG-1 Fathom and partner platforms for anti-submarine warfare.
  name: Underwater Surveillance and ASW
- description: Use Altra to fuse multi-drone and multi-sensor feeds for targeting and strike coordination.
  name: Reconnaissance-Strike Coordination
website: https://helsing.ai
---
