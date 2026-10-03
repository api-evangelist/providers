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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 27
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering public product road map publishing, feature voting, customer feedback aggregation, and product discovery surfaces. Public road map platforms expose what a product team is building, what is shipping next, and what is being considered, while feature voting and feedback portals route customer signal back into product planning. This collection brings together dedicated road map and feedback platforms like Productboard, Canny, Aha.io, Pendo, and Userpilot, alongside product work management systems like Linear, Jira, Trello, and Notion that increasingly expose road map and planning surfaces, and announcement and discovery surfaces like LaunchNotes, AnnounceKit, Beamer, and Product Hunt that publish what shipped.
examples:
- key_count: 9
  name: Road Map Feature Vote Example
  slug: road-map-feature-vote-example
- key_count: 16
  name: Road Map Roadmap Item Example
  slug: road-map-roadmap-item-example
features:
- description: Dedicated road map platforms like Productboard, Aha.io, and LaunchNotes expose a public view of what is now, next, and later, giving customers a structured window into product direction without leaking internal tracker noise.
  name: Public Road Map Publishing
- description: Feature voting portals like Canny, Productboard, and Userback collect customer ideas and votes, then rank and route them back to product teams as prioritized signal.
  name: Feature Voting and Idea Capture
- description: Road map APIs expose releases, milestones, and ship dates as first-class resources, letting downstream sites, customer success tools, and changelogs syndicate what shipped and what is coming.
  name: Release and Milestone Surfaces
- description: Platforms like Canny, Productboard, and Pendo aggregate feedback threads from email, in-app widgets, and CRMs, then attach those threads to road map items so impact and demand stay attached to features.
  name: Feedback Thread Aggregation
- description: Work management tools like Linear, Jira, Trello, Asana, ClickUp, and Monday.com expose plan, cycle, and milestone APIs that increasingly double as the source of truth for public road maps.
  name: Work Management Road Maps
- description: Announcement platforms like LaunchNotes, AnnounceKit, Beamer, and Product Hunt publish what shipped, turning closed road map items into customer-facing changelog entries and product discovery surfaces.
  name: Changelog and Discovery Channels
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Product management platform with public road map, feature portals, and customer feedback aggregation tied to a prioritized planning surface.
  name: Productboard
- description: Customer feedback and feature voting platform with public road map views, changelog, and Intercom, Zendesk, and Slack integrations.
  name: Canny
- description: Road map and strategy platform exposing releases, features, ideas, and goals via a structured product planning API.
  name: Aha.io
- description: Software project tracker exposing projects, cycles, roadmaps, and milestones via GraphQL, used as the source of truth for many public road maps.
  name: Linear
- description: Atlassian work tracker exposing plans, advanced road maps, and release versions via REST and Forge APIs for public road map syndication.
  name: Jira
- description: Product experience platform with road map, feedback, and in-app guides tied to product usage analytics.
  name: Pendo
- description: Public road map, changelog, and release communication platform that publishes what shipped and what is coming with API-driven syndication.
  name: LaunchNotes
- description: Visual board tool from Atlassian widely used as a lightweight public road map via shared boards and the Trello REST API.
  name: Trello
json_schemas:
- name: FeatureVote
  property_count: 9
  slug: road-map-feature-vote
- name: RoadmapItem
  property_count: 16
  slug: road-map-roadmap-item
json_structures:
- name: Road Map Feature Vote Structure
  property_count: 9
  slug: road-map-feature-vote-structure
- name: Road Map Roadmap Item Structure
  property_count: 16
  slug: road-map-roadmap-item-structure
jsonld:
- class_count: 10
  name: Road Map Context
  property_count: 20
  slug: road-map-context
layout: provider
modified: '2026-05-19'
name: Road Map
nav: Providers
network: true
overview: 'Road Map is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Roadmaps, Product Discovery, Feature Voting, Public Roadmap, and Customer Feedback.


  The Road Map catalog on APIs.io includes 1 JSON-LD context.


  Road Map''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: road-map
tags:
- Roadmaps
- Product Discovery
- Feature Voting
- Public Roadmap
- Customer Feedback
use_cases:
- description: Product teams publish a curated public road map via Productboard, Aha.io, or Canny so prospects, customers, and partners can see what is shipping and what is being considered.
  name: Customer-Facing Public Road Map
- description: Companies operate a Canny or Productboard portal where customers submit and upvote feature requests, with the highest-signal items getting promoted to the public road map.
  name: Feature Request Voting Portal
- description: Customer success and sales teams pull live road map data via API into CRMs, briefings, and proposals so customer conversations stay grounded in real ship dates rather than aspirational decks.
  name: Sales and Customer Success Visibility
- description: Engineering teams running on Linear, Jira, or Shortcut sync a filtered slice of their internal plans to a public road map surface, keeping internal velocity and external promises in lockstep.
  name: Engineering Plan to Public Road Map Sync
- description: Teams use LaunchNotes, AnnounceKit, or Beamer to convert closed road map items into changelog entries and in-app announcements that close the loop with users who voted for the work.
  name: Changelog and Launch Announcements
- description: AI agents and copilots query road map APIs to answer customer questions about feature availability, ship dates, and parity gaps using grounded, governed data rather than scraped marketing pages.
  name: AI Agent Road Map Awareness
website: https://apievangelist.com
---
