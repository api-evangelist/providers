---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: 'Core Redux library for managing application state through a predictable unidirectional data flow. The library exposes createStore, combineReducers, applyMiddleware, compose, and bindActionCreators as '
  name: Redux Core API
  slug: redux-core-api
- description: Official React bindings for Redux, enabling React components to interact with a Redux store. Provides hooks (useSelector, useDispatch, useStore) and a Provider component for connecting the Redux store
  name: React Redux API
  slug: react-redux-api
- description: The official, opinionated, batteries-included toolset for efficient Redux development. Redux Toolkit simplifies common Redux use cases including store setup, creating reducers and writing immutable up
  name: Redux Toolkit API
  slug: redux-toolkit-api
- description: Developer tools for debugging Redux applications with time-travel debugging capabilities. The Redux DevTools Extension allows inspection of every state and action payload dispatched, going back in tim
  name: Redux DevTools API
  slug: redux-devtools-api
- description: A Redux middleware library that aims to make application side effects such as asynchronous data fetching and accessing browser caches easier to manage and more efficient to execute. Uses ES6 Generator
  name: Redux Saga
  slug: redux-saga
- description: RxJS-based middleware for Redux. Compose and cancel async actions to create side effects and more using Epics. An epic is a function which takes a stream of actions and returns a stream of actions.
  name: Redux Observable
  slug: redux-observable
- description: Thunk middleware for Redux, included by default with Redux Toolkit. Allows writing action creators that return a function instead of an action object, enabling delayed dispatch and conditional dispatc
  name: Redux Thunk
  slug: redux-thunk
- description: A selector library for Redux. Selectors are functions that compute derived data from the Redux state, allowing Redux to store the minimal possible state. Reselect creates memoized selector functions t
  name: Reselect
  slug: reselect
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redux-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://redux.js.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reduxjs
- group: company
  title: ''
  type: Blog
  url: https://blog.isquaredsoftware.com/
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/redux
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/reduxjs
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/redux
- group: docs
  title: ''
  type: StyleGuide
  url: https://redux.js.org/style-guide/style-guide
- group: operate
  title: ''
  type: FAQ
  url: https://redux.js.org/faq
- group: learn
  title: ''
  type: Tutorials
  url: https://redux.js.org/tutorials/essentials/part-1-overview-concepts
- group: commercial
  title: ''
  type: License
  url: https://github.com/reduxjs/redux/blob/master/LICENSE.md
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/redux-store-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/redux-action-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/redux-store-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/redux-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/redux-vocabulary.yml
created: '2024-01-15'
description: Redux is a predictable state container for JavaScript apps. It helps write applications that behave consistently, run in different environments (client, server, and native), and are easy to test. Redux provides a single immutable state tree, pure reducer functions for state transitions, and a unidirectional data flow pattern based on the Flux architecture. The Redux ecosystem includes React Redux for React bindings, Redux Toolkit for simplified development patterns, and Redux DevTools for time-travel debugging. Redux is widely used with React but can be paired with any JavaScript view library.
finops:
- name: Redux Finops
  service_category: API
  slug: redux-finops
image: https://redux.js.org/img/redux-logo-landscape.png
json_schemas:
- name: Redux Action
  property_count: 4
  slug: redux-action
- name: Redux Store
  property_count: 4
  slug: redux-store
json_structures:
- name: Redux Store Structure
  property_count: 0
  slug: redux-store-structure
jsonld:
- class_count: 9
  name: Redux Context
  property_count: 11
  slug: redux-context
layout: provider
modified: '2026-05-02'
name: Redux
nav: Providers
network: true
overview: 'Redux publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Flux Architecture, Frontend, Javascript, Predictable State, and React.


  The Redux catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Redux''s developer surface includes engineering blog, Stack Overflow tag, FAQ, and 13 more developer resources.'
plans:
- name: Redux Plans Pricing
  plan_count: 3
  slug: redux-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Redux Rate Limits
  slug: redux-rate-limits
rules:
- name: Redux API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: redux-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.1
  delta: -5.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 17.7
    developer_ergonomics: 6.5
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 39.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/redux/refs/heads/main/screenshots/redux-2026-06-20T192739.png
security:
- kind: domain-security
  name: Redux Domain Security
  slug: redux-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: redux
tags:
- Flux Architecture
- Frontend
- Javascript
- Predictable State
- React
- State Management
- Typescript
website: https://redux.js.org
---
