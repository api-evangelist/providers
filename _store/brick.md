---
aid: brick
url: https://raw.githubusercontent.com/api-evangelist/brick/refs/heads/main/apis.yml
name: BRICK Schema
tags:
  - Building Information Modeling
  - BIM
  - Smart Buildings
  - Ontology
  - Semantic Web
  - IoT
  - HVAC
  - Energy Management
type: Index
x-type: standard
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: Open
created: '2025-02-17'
modified: '2026-04-21'
position: Consumer
description: BRICK is an open-source community-driven ontology standard for standardizing semantic descriptions of physical, logical, and virtual assets in buildings and the relationships between them. Using Semantic Web (RDF/OWL) technology, BRICK v1.4.4 enables interoperability across building management systems, reducing the cost of deploying analytics and energy efficiency initiatives. It supports HVAC, lighting, fire, security, and other building subsystems under a unified extensible vocabulary with SHACL-based validation.
apis:
  - aid: brick:ontology
    name: BRICK Ontology
    tags:
      - Ontology
      - RDF
      - OWL
      - Building Systems
      - Semantic Web
    humanURL: https://brickschema.org/
    properties:
      - url: https://brickschema.org/
        type: Website
      - url: https://docs.brickschema.org/
        type: Documentation
      - url: https://ontology.brickschema.org/
        type: OntologyBrowser
      - url: https://github.com/BrickSchema/Brick
        type: GitHubRepository
    description: The BRICK ontology v1.4.4 defines a standardized vocabulary of building system concepts, relationships, and data model for smart building analytics. Available as RDF/OWL files, BRICK describes sensors, equipment, locations, and control points in HVAC, lighting, fire safety, and security systems. Includes SHACL shapes for ontology validation and Python tooling via the brickschema Python package.
common:
  - type: Website
    url: https://brickschema.org/
  - type: Documentation
    url: https://docs.brickschema.org/
  - type: GitHubOrganization
    url: https://github.com/BrickSchema
  - type: GitHubRepository
    url: https://github.com/BrickSchema/Brick
  - type: OntologyBrowser
    url: https://ontology.brickschema.org/
  - type: Community
    url: https://groups.google.com/g/brickschema
  - type: PyPIPackage
    url: https://pypi.org/project/brickschema/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
