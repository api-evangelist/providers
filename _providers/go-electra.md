---
api_count: 1
artifact_total: 0
created: '2026-08-17'
description: 'Electra is a European operator of ultra-fast electric-vehicle charging, headquartered at 104 rue de Richelieu in the 2nd arrondissement of Paris and led by co-founder and CEO Aurelien de Meaux. It designs, finances, installs and operates its own DC fast-charging stations rather than reselling someone else''s hardware, advertising 770+ live stations with 68 more under construction, charge rates up to 400 kW, and a target of 2,200 stations / 15,000 charge points across Europe by 2030. Its own pricing and station pages cover France, Belgium, Spain, Italy, Germany, Austria, the Netherlands and Switzerland, with city hubs in Paris, Lyon, Marseille, Brussels, Antwerp, Liege, Milan, Bologna, Turin, Madrid, Barcelona and Zurich. The commercial surface is consumer- and fleet-facing: a mobile app, an Electra+ subscription that cuts up to 0.20 EUR/kWh, an RFID charging card, Autocharge and Plug&Charge, and a fleet dashboard at business.go-electra.com. It is a Serena portfolio company
  and has raised a 160 MEUR round, a 304 MEUR Series B and a 433 MEUR debt facility. Electra publishes NO developer portal, NO API documentation, NO OpenAPI, NO llms.txt, NO MCP server and NO A2A agent card — every one of those was probed and missed on 2026-08-17. What it does run, and what almost nobody looking at the marketing site would find, is a real machine-readable API: a live Open Charge Point Interface implementation in the Charge Point Operator role at https://ocpi.go-electra.com/ocpi/cpo, serving BOTH OCPI 2.1.1 and OCPI 2.2.1 concurrently. Its version-negotiation endpoints answer anonymously with HTTP 200 and enumerate the full module inventory — cdrs, commands, credentials, locations, sessions, tariffs and tokens, with SENDER/RECEIVER roles declared on the 2.2.1 surface — while every data module itself returns HTTP 401 with `WWW-Authenticate: Token realm="Application"`, OCPI''s own bilateral token scheme. That is a documented open industry standard, fully implemented, discoverable
  without credentials and readable only with a roaming agreement; its production use is evidenced by the 180+ e-mobility service provider cards Electra''s own help centre lists as accepted at its chargers.'
image: https://www.go-electra.com/favicons/apple-touch-icon-1024x1024.png
layout: provider
modified: '2026-08-17'
name: Electra
nav: Providers
network: true
random_paper: 101
slug: go-electra
tags:
- Company
- Climate Tech
- EV Charging
- Energy
- Mobility
- OCPI
- Roaming
- Charge Point Operator
- Electric Vehicles
- Fast Charging
- Charging Sessions
- Tariffs
- Electrification
- France
- Europe
---
