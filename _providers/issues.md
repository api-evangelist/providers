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
artifact_total: 30
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
description: An index and topic collection covering issue tracking, bug tracking, and project-management APIs that expose issue, ticket, task, and work-item primitives. Issue tracking APIs are the connective tissue between engineering, product, and operations work — they capture defects, feature requests, user stories, and tasks, then move them through configurable workflows from creation to resolution. This collection includes developer-centric trackers like Jira, Linear, GitHub Issues, and GitLab Issues; project- and work-management platforms like Asana, ClickUp, Monday.com, Trello, and Wrike; product-discovery trackers like Productboard and Shortcut; classic open-source bug trackers like Redmine; and flexible work-item stores like Notion, Airtable, and Smartsheet. It is distinct from the customer-support topic (Zendesk-style help desks) and from incident management (which lives under monitoring).
examples:
- key_count: 10
  name: Issues Comment Example
  slug: issues-comment-example
- key_count: 15
  name: Issues Issue Example
  slug: issues-issue-example
features:
- description: Issue tracking APIs expose a core issue/ticket primitive with identifier, title, description, status, assignee, reporter, priority, and timestamps as the unit of work that flows through development and project workflows.
  name: Issue and Ticket Primitives
- description: Trackers like Jira, Linear, and Azure DevOps model state machines on top of issues — open, in-progress, in-review, done — and expose transition APIs that move work between states with optional validations and side effects.
  name: Configurable Workflows and Transitions
- description: Issue APIs let teams classify work using labels, tags, components, fix versions, epics, and arbitrary custom fields, which are first-class resources that can be created, listed, and assigned via the API.
  name: Labels, Components, and Custom Fields
- description: Issues accumulate conversation and history. Most trackers expose comments as a separate resource and provide an audit-style activity stream covering field changes, transitions, and attachments.
  name: Comments and Activity Streams
- description: Agile-oriented APIs (Jira Agile, Linear, Shortcut, Azure Boards) expose sprints, iterations, kanban boards, and backlogs as objects you can query and mutate alongside the underlying issues.
  name: Sprints, Boards, and Backlogs
- description: Issue trackers publish events (created, updated, transitioned, commented) over webhooks so external automations, chatops bots, CI systems, and AI agents can react to work-item changes in near real time.
  name: Webhooks and Event Subscriptions
- description: Trackers expose query languages or filter parameters (Jira's JQL, GitHub's search syntax, Linear's filter API) for finding issues by status, assignee, label, sprint, or arbitrary custom-field combinations.
  name: Search, JQL, and Saved Queries
- description: Issues support file attachments and relationships to other issues (blocks, blocked-by, duplicates, relates-to) and to external artifacts like commits, pull requests, deploys, and design files.
  name: Attachments and Linked Resources
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Atlassian's market-leading issue and project tracker for software teams, with a deep REST API covering issues, projects, sprints, JQL search, custom fields, and webhooks.
  name: Jira
- description: Modern, opinionated issue tracker for high-velocity software teams, with a first-class GraphQL API for issues, cycles, projects, and roadmaps.
  name: Linear
- description: Lightweight tracker built into GitHub repositories, accessible through the GitHub REST and GraphQL APIs alongside pull requests, commits, and Actions.
  name: GitHub Issues
- description: Issue tracker tightly integrated with GitLab repositories, CI/CD, and merge requests, exposed via the GitLab REST and GraphQL APIs.
  name: GitLab Issues
- description: Work-management platform with tasks, projects, sections, and custom fields, exposed via the Asana REST API and frequently used as a cross-functional issue tracker.
  name: Asana
- description: All-in-one work-management platform with tasks, lists, spaces, and views, accessible through the ClickUp REST API.
  name: ClickUp
- description: Visual work-management platform with boards, items, and columns, accessible through the Monday GraphQL API and widely used as a task and issue tracker.
  name: Monday.com
- description: Microsoft's developer platform whose Boards service provides work-item tracking (bugs, user stories, tasks, epics) via the Azure DevOps REST API.
  name: Azure DevOps
json_schemas:
- name: Comment
  property_count: 10
  slug: issues-comment
- name: Issue
  property_count: 15
  slug: issues-issue
json_structures:
- name: Issues Comment Structure
  property_count: 10
  slug: issues-comment-structure
- name: Issues Issue Structure
  property_count: 15
  slug: issues-issue-structure
jsonld:
- class_count: 10
  name: Issues Context
  property_count: 16
  slug: issues-context
layout: provider
modified: '2026-05-19'
name: Issues
nav: Providers
network: true
overview: 'Issues is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Issue Tracking, Bug Tracking, Project Management, Task Management, and Work Management.


  The Issues catalog on APIs.io includes 1 JSON-LD context.


  Issues'' developer surface includes developer portal and 1 more developer resources.'
random_paper: 8
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
slug: issues
tags:
- Issue Tracking
- Bug Tracking
- Project Management
- Task Management
- Work Management
use_cases:
- description: Software teams use Jira, Linear, GitHub Issues, or GitLab Issues as the system of record for bugs, stories, and tasks, with API integrations into IDEs, CI/CD pipelines, and code review tools.
  name: Engineering Issue Tracking
- description: Work-management platforms like Asana, ClickUp, Monday.com, and Wrike coordinate tasks across engineering, marketing, design, and operations, often syncing with developer trackers via API.
  name: Cross-Team Work Coordination
- description: Productboard, Shortcut, and Linear connect customer feedback and product opportunities to issues and roadmap items, exposing APIs for ingesting feedback and synchronizing with engineering work.
  name: Product Roadmap and Discovery
- description: Slack, Microsoft Teams, and Discord bots create, update, transition, and comment on issues using tracker APIs — turning chat messages into tickets and pushing status updates back into channels.
  name: ChatOps and Bot Automation
- description: AI agents use issue tracker APIs to classify incoming issues, suggest labels and assignees, summarize threads, draft replies, link related tickets, and propose status transitions for human review.
  name: AI Agent Triage and Routing
- description: BI tools and dashboards pull cycle time, throughput, lead time, and backlog metrics from issue tracker APIs to measure engineering productivity and project health.
  name: Reporting, Dashboards, and Analytics
- description: Backstage, Compass, and other internal developer portals embed issue tracker data alongside services, deployments, and ownership so teams see open issues for the components they own.
  name: Internal Developer Portals
website: https://apievangelist.com
---
