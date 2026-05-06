---
aid: scorm
name: SCORM
description: SCORM (Sharable Content Object Reference Model) is a set of technical standards for e-learning software products. Originally developed by the Advanced Distributed Learning (ADL) Initiative, SCORM defines how online learning content and Learning Management Systems (LMS) communicate with each other, enabling interoperability between authoring tools, content packages, and LMS platforms. Key versions include SCORM 1.2 and SCORM 2004, with xAPI (Tin Can) as a modern successor.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - E-Learning
  - LMS
  - Standards
  - Education
  - Interoperability
created: '2026-05-02'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/scorm/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: scorm:scorm-12
    name: SCORM 1.2 Runtime API
    description: The SCORM 1.2 Run-Time Environment defines communication between e-learning content and an LMS via a JavaScript API. The API Adapter is an ECMAScript object named "API" accessible through the DOM. It enables content to initialize sessions, get and set CMI data model values, commit data, and retrieve error information.
    humanURL: https://scorm.com/scorm-explained/technical-scorm/scorm-12-overview-for-developers/
    tags:
      - E-Learning
      - LMS
      - Standards
      - SCORM 1.2
    properties:
      - type: Documentation
        url: https://scorm.com/scorm-explained/technical-scorm/scorm-12-overview-for-developers/
      - type: Specification
        url: https://adlnet.gov/projects/scorm/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/scorm/refs/heads/main/json-schema/scorm-cmi-data-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/scorm/refs/heads/main/json-structure/scorm-package-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/scorm/refs/heads/main/json-ld/scorm-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/scorm/refs/heads/main/vocabulary/scorm-vocabulary.yml
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/scorm/refs/heads/main/examples/scorm-api-initialize-example.json
  - aid: scorm:scorm-2004
    name: SCORM 2004 Runtime API
    description: The SCORM 2004 Run-Time Environment extends SCORM 1.2 with improved sequencing and navigation capabilities. The API Adapter is an ECMAScript object named "API_1484_11". It supports 8 core API functions for session management, data model access, and error reporting, plus a richer CMI data model with completion status, success status, score, and interaction tracking.
    humanURL: https://scorm.com/scorm-explained/technical-scorm/scorm-2004-overview-for-developers/
    tags:
      - E-Learning
      - LMS
      - Standards
      - SCORM 2004
    properties:
      - type: Documentation
        url: https://scorm.com/scorm-explained/technical-scorm/scorm-2004-overview-for-developers/
      - type: Specification
        url: https://adlnet.gov/projects/scorm/
  - aid: scorm:xapi
    name: xAPI (Experience API / Tin Can)
    description: xAPI (Experience API), also known as Tin Can API, is the modern successor to SCORM developed by ADL. It uses a Learning Record Store (LRS) and defines learning statements in a subject-verb-object format, enabling tracking of a much wider range of learning experiences beyond traditional LMS-hosted content.
    humanURL: https://xapi.com/
    tags:
      - E-Learning
      - Standards
      - xAPI
      - Tin Can
    properties:
      - type: Documentation
        url: https://xapi.com/overview/
      - type: Specification
        url: https://github.com/adlnet/xAPI-Spec
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
