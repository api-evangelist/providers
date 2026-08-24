/*! Kin Score glyph — the K'in sun.
 *  Generated from kin-glyph.js by build.mjs. Do not edit here.
 *  Canonical source: api-evangelist/kin-score/glyph/
 *  Spec: api-evangelist/kin-score/glyph/GLYPH.md
 */
(function (root) {
  'use strict';

/*
 * Kin Score glyph — the K'in sun.
 *
 * Core  : concentric rings, one per Kin Score facet, filled clockwise to that
 *         facet's score. Ring colour depends on the palette (see PALETTES).
 * Rays  : 12 triangles around the outside, one per agent-readiness dimension,
 *         solid when the dimension is satisfied — the sun's rays.
 *
 * Zero dependencies. Returns an SVG string, so it renders identically at build
 * time, at runtime, and inside a PNG pipeline.
 */

/* Each facet owns a fixed hue, in fixed order. Categorical colour encodes
   IDENTITY (which facet this is), never rank — arc length carries the score.
   This is the Apple Activity model: Move/Exercise/Stand are always red/green/
   blue however well you did. It is also what keeps the glyph colourful for
   every provider, including one scoring uniformly high, where colouring by
   band collapses to a single hue.
   Hues are slots 1-6 of the design system's validated categorical theme.
   Validated `--pairs adjacent`: ALL CHECKS PASS in both light and dark. */
const FACETS = [
  { id: 'discoverability',          label: 'Discoverability',          light: '#2a78d6', dark: '#3987e5' },
  { id: 'contract_quality',         label: 'Contract Quality',         light: '#eb6834', dark: '#d95926' },
  /* `governance` and `commercial_clarity` keep their IDs and their hues; only the
     labels moved. Rubric 0.12 renamed them to "Contract Governance" and "Access
     Clarity" and emits each score under BOTH the old id and a new alias
     (`emits_as` in scoring.yml), so the id here still resolves and no ring was
     ever missing — the badge just went on asserting the retired names. The rename
     was substantive: scoring.yml's own note says Governance "never measured how
     the organisation governs itself, and the standalone accountability layer now
     does, so one word could not carry both." Relabelled 0.12, roadmap#89.
     DO NOT rename the IDs to the aliases. The positional encodings key off these
     ids, and the scorer writes both names, so the short one still resolves. */
  { id: 'governance',               label: 'Contract Governance',      light: '#1baf7a', dark: '#199e70' },
  { id: 'operational_transparency', label: 'Operational Transparency', light: '#eda100', dark: '#c98500' },
  { id: 'developer_ergonomics',     label: 'Developer Ergonomics',     light: '#e87ba4', dark: '#d55181' },
  { id: 'commercial_clarity',       label: 'Access Clarity',           light: '#008300', dark: '#008300' },
];

/* One ray per agent-readiness dimension, in scoring.yml order. MUST stay in
   sync with `agent_readiness.dimensions` in scoring.yml and with DIM_ORDER in
   network/scripts/build_listings.py — the compact encoding is POSITIONAL, so
   reordering here is a breaking change.

   Fourteen as of 0.6. Was twelve at 0.4; `agent_card` shipped in 0.5.1 and was
   never drawn, so for two days the sun was silently a ray short of the score it
   was illustrating. `dry_run_mode` is new in 0.6.

   Slot 8 was `asyncapi_events` until rubric 0.9 renamed and widened it to
   `event_surface_described` — it had read only the asyncapi/ directory, naming the
   artifact rather than the capability, and so scored false for the 125 providers who
   describe their event surface in OpenAPI `webhooks`/`callbacks` instead. The rename
   was not carried here or into build_listings.py, so the index builder dropped the
   dimension from every badge with a warning nobody was reading. Same slot, same label,
   so this is a rename and not a reordering.

   FIFTEEN as of 0.12: `reversibility_documented` was added to the rubric and never
   drawn here, so for every provider, on every badge, the ray simply did not exist —
   the same failure as `agent_card` at 0.5.1 and `asyncapi_events` at 0.9, printing
   the same warning nobody read. Third time. roadmap#89.

   IT IS APPENDED AT SLOT 15, NOT INSERTED AT SLOT 3 WHERE scoring.yml PUTS IT.
   That divergence is deliberate, and it is the one thing to understand before
   touching this list. Two things consume the positional encoding and only one of
   them is self-describing:

     - the badge shard carries its own `dim_order` and the badge Lambda decodes
       against THAT (lambdas/badge/data.mjs), so a stale shard still decodes
       correctly. Insertion would have been safe here.
     - the trit string in provider_bands.yml has no such header. The browser glyph
       decodes it against whatever DIMENSIONS its own vendored bundle happens to
       carry. Insert at slot 3 and every asset/data skew silently shifts twelve
       dimensions — each ray reporting its neighbour's grade, with nothing to show
       anything is wrong.

   Appending shifts nothing: an encoding written before this lands is decoded
   identically, and the new slot reads absent until the next build fills it. The
   only cost is that ray order no longer matches scoring.yml order, which is
   invisible — the rays sit on a circle and each carries its own label. Prefer that
   cost every time. If a dimension is ever genuinely REMOVED, retire its slot in
   place rather than closing the gap. */
const DIMENSIONS = [
  { id: 'spec_presence',      label: 'Machine-Readable Contract' },
  { id: 'agentic_access',     label: 'Agentic Access Contract' },
  { id: 'mcp_server',         label: 'MCP Server' },
  { id: 'auth_clarity',       label: 'Machine-Readable Auth' },
  { id: 'idempotency',        label: 'Idempotency' },
  { id: 'error_semantics',    label: 'Stable Error Semantics' },
  { id: 'openapi_examples',   label: 'Request/Response Examples' },
  { id: 'rate_limit_signal',  label: 'Rate-Limit Signaling' },
  { id: 'event_surface_described', label: 'Typed Event Surface' },
  { id: 'agent_skills',       label: 'Agent Skills' },
  { id: 'well_known_catalog', label: 'Well-Known Catalog' },
  { id: 'consent_identity',   label: 'Consent & Bot Identity' },
  { id: 'agent_card',         label: 'A2A Agent Card' },
  { id: 'dry_run_mode',       label: 'Dry-Run / Simulate Mode' },
  // Slot 15, appended 0.12 — see the note above on why this is not at slot 3.
  { id: 'reversibility_documented', label: 'Documented Reversibility' },
  // Slot 16, appended 0.13.0 (roadmap#99) — same rule as slot 15.
  { id: 'delegated_identity', label: 'Delegated User Identity' },
  // Slots 17-18, appended 0.13.0 (roadmap#98) — RFC 9728 and RFC 7591.
  { id: 'protected_resource_metadata', label: 'Protected Resource Metadata' },
  { id: 'dynamic_client_registration', label: 'Registration Without a Human' },
  // Slot 19, appended 0.13.0 (roadmap#123).
  { id: 'agentic_commerce', label: 'Agentic Commerce Surface' },
];

/* Grades that mean PARTIAL credit rather than full. 0.6 made seven of the
   fourteen dimensions capable of landing here — four graded on evidence
   (`documented`, `partial`) and three graded on authorship (`derived`,
   `mixed`), plus the agent card's own conformance ladder.

   A partial ray is drawn SHORT and solid rather than faded: opacity does not
   survive greyscale, print or forced-colors, and the whole point of the
   silhouette is that it reads at a glance. A stubby ray says "there, but not
   all the way there" in any rendering. */
const PARTIAL_GRADES = new Set([
  'documented', 'partial', 'derived', 'mixed', 'conformance',
  'near-conformant', 'flavored',
  // 0.12.2 (roadmap#97) — auth_clarity grades: bound 1.00 / negotiable 0.75 / bearer 0.35.
  // `bound` is deliberately absent: full credit draws a full ray. Without the other two,
  // rayState() falls through to its `return 'full'` default and an apiKey-only provider
  // earning 3.5 of 10 draws a ray identical to a mutualTLS provider earning all ten --
  // the exact thing partial grading exists to prevent.
  'negotiable', 'bearer',
  // 0.13 (roadmap#102) — the OIDC-discovery tier, 0.90. NOT called `verified`: that string
  // already means 1.00 in five other dimensions and rayState() returns 'full' for it.
  'served',
  // 0.13.0 (roadmap#123) — agentic_commerce `platform` at 0.25.
  'platform',
]);

/* off | partial | full — from a bool, a grade string, or a trit char. */
function rayState(v) {
  if (v === true || v === 1 || v === '1') return 'full';
  if (v === false || v === 0 || v === '0' || v == null) return 'off';
  if (v === 2 || v === '2') return 'partial';
  const s = String(v).toLowerCase();
  if (PARTIAL_GRADES.has(s)) return 'partial';
  return 'full';   // 'verified', 'conformant', 'first-party'
}

// Band thresholds, high → low (scoring.yml `bands`). Re-cut at Kin Score 0.6.
const BANDS = [
  { id: 'exemplar',   label: 'Exemplar',   min: 66 },
  { id: 'strong',     label: 'Strong',     min: 56 },
  { id: 'developing', label: 'Developing', min: 42 },
  { id: 'thin',       label: 'Thin',       min: 28 },
  { id: 'emerging',   label: 'Emerging',   min: 13 },
  { id: 'minimal',    label: 'Minimal',    min: 0  },
];

const PALETTES = {
  /* ORDINAL — one hue family, 38 deg traverse (cyan -> deep indigo).
     Validated --ordinal: ALL CHECKS PASS on both surfaces. Rank is readable
     from colour alone and survives greyscale — but a uniformly-strong provider
     comes out near-monochrome. */
  ordinal: {
    light: {
      surface: '#f8f9fa',
      exemplar: '#002e7b', strong: '#005295', developing: '#1575ae',
      thin: '#3999c5', emerging: '#5ebcdc', minimal: '#c2c7cf',
      track: '#dfe3e8', ink: '#12172b', muted: '#5b6270', rayOff: '#8b93a3',
    },
    dark: {
      surface: '#1a1a2e',
      exemplar: '#87dfff', strong: '#65bbe6', developing: '#4897cd',
      thin: '#3173b4', emerging: '#234f99', minimal: '#4a5162',
      track: '#343850', ink: '#f3f5f8', muted: '#9aa2b4', rayOff: '#7f88a0',
    },
  },
  /* BRIGHT — distinct hues per BAND. Easy to tell bands apart, impossible to
     rank without the legend. Light passes with reliefs; dark does not (no five
     hues in that column are mutually separable). Kept for comparison. */
  bright: {
    light: {
      surface: '#f8f9fa',
      exemplar: '#4a3aa7', strong: '#2a78d6', developing: '#1baf7a',
      thin: '#eda100', emerging: '#e34948', minimal: '#c2c7cf',
      track: '#dfe3e8', ink: '#12172b', muted: '#5b6270', rayOff: '#8b93a3',
    },
    dark: {
      surface: '#1a1a2e',
      exemplar: '#9085e9', strong: '#3987e5', developing: '#199e70',
      thin: '#c98500', emerging: '#e66767', minimal: '#4a5162',
      track: '#343850', ink: '#f3f5f8', muted: '#9aa2b4', rayOff: '#7f88a0',
    },
  },
};

/* FACET — rings take their own facet's hue (see FACETS), so the glyph is
   always full of colour. Rank moves to the centre: the band name under the
   number. Chrome (track/ink/muted) is shared with the ordinal palette. */
PALETTES.facet = {
  light: { ...PALETTES.ordinal.light },
  dark:  { ...PALETTES.ordinal.dark  },
};

/* RAYS — a warm gold ramp of their own, keyed to the agent-readiness band, so
   the sun's rays read as sunlight rather than as more of the core palette. Held
   deliberately apart from every ring hue: nothing in FACETS is warm-gold, so a
   ray can never be mistaken for a facet.
   The ramp BRIGHTENS with readiness: agent-native is the most luminous gold the
   light surface will carry (#dea800, 2.05:1 — the contrast floor is what stops
   it going brighter still), agent-aware and below fall away into amber. On dark
   it opens right up to #ffd060.
   Validated --ordinal: ALL CHECKS PASS on both surfaces. */
const RAYS = {
  light: {
    'agent-native': '#dea800', 'agent-ready': '#cf8700',
    'agent-aware':  '#bd6800', 'human-only':  '#a94900',
  },
  dark: {
    'agent-native': '#ffd060', 'agent-ready': '#e9a738',
    'agent-aware':  '#d07e0b', 'human-only':  '#b45600',
  },
};

// Back-compat.
const RAMP = PALETTES.ordinal;

function bandOf(score) {
  for (const b of BANDS) if (score >= b.min) return b.id;
  return 'minimal';
}

const esc = (s) => String(s).replace(/[&<>"]/g, (c) =>
  ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

/**
 * @param {object} p     {name, score, band, agent_score, agent_band, facets, agent_dims}
 * @param {object} opts  {size, mode:'light'|'dark', palette:'facet'|'ordinal'|'bright',
 *                        showRays, coreFill, title}
 * @returns {string} SVG markup
 */
function kinGlyph(p, opts = {}) {
  const size = opts.size || 240;
  const mode = opts.mode || 'light';
  const palette = opts.palette || 'facet';
  const C = (PALETTES[palette] || PALETTES.facet)[mode];
  const showRays = opts.showRays !== false;
  const cx = size / 2, cy = size / 2;

  const rayBand = showRays ? size * 0.115 : 0;
  const outerR  = size / 2 - rayBand - size * 0.02;
  const coreR   = size * 0.163;   // room for the band label under the number
  const gap     = Math.max(2, size * 0.018);
  const ringW   = (outerR - coreR - gap * (FACETS.length - 1)) / FACETS.length;

  const parts = [];

  // --- facet rings --------------------------------------------------------
  // stroke-dasharray on a circle gives rounded data-ends and needs no arc maths.
  FACETS.forEach((f, i) => {
    const raw = Number(p.facets?.[f.id] ?? 0);
    const v = Math.max(0, Math.min(100, raw));
    const r = outerR - ringW / 2 - i * (ringW + gap);
    const circ = 2 * Math.PI * r;
    const band = bandOf(v);
    const col = palette === 'facet' ? f[mode] : C[band];

    // The TRACK carries the hover hooks, so the whole ring is hoverable —
    // including a facet scoring zero, where there is no filled arc to hit.
    const hooks =
      `data-kind="ring" data-label="${esc(f.label)}" ` +
      `data-value="${raw.toFixed(1)}" data-band="${band}"`;
    const tip = `<title>${esc(f.label)}: ${raw.toFixed(1)} (${band})</title>`;

    parts.push(
      `<circle cx="${cx}" cy="${cy}" r="${r.toFixed(2)}" fill="none" ` +
      `stroke="${C.track}" stroke-width="${ringW.toFixed(2)}" ${hooks}>${tip}</circle>`);

    if (v > 0) {
      const on = (v / 100) * circ;
      parts.push(
        `<circle cx="${cx}" cy="${cy}" r="${r.toFixed(2)}" fill="none" ` +
        `stroke="${col}" stroke-width="${ringW.toFixed(2)}" stroke-linecap="round" ` +
        `stroke-dasharray="${on.toFixed(2)} ${(circ - on).toFixed(2)}" ` +
        `transform="rotate(-90 ${cx} ${cy})" ${hooks}>${tip}</circle>`);
    }
  });

  // --- agent-readiness rays ----------------------------------------------
  if (showRays) {
    const agentBand = p.agent_band || 'human-only';
    const rayCol = RAYS[mode][agentBand] || RAYS[mode]['human-only'];
    const baseR = outerR + size * 0.022;
    const tipR = baseR + rayBand * 0.72;
    const halfW = (Math.PI * 2 * baseR) / DIMENSIONS.length * 0.30;
    // Unsatisfied rays get a heavier, darker outline than the ring track so the
    // sun's silhouette survives greyscale, print and forced-colors.
    const strokeW = Math.max(1.25, size * 0.0125);

    DIMENSIONS.forEach((d, i) => {
      const a = (i / DIMENSIONS.length) * Math.PI * 2 - Math.PI / 2;
      const raw = p.agent_dims?.[d.id];
      const state = rayState(raw);
      // A partial ray reaches 55% of the way out. Solid, so it still reads as a
      // ray; short, so the shortfall is visible without colour or opacity.
      const reach = state === 'partial' ? 0.55 : 1;
      const thisTipR = baseR + (tipR - baseR) * reach;
      const px = Math.cos(a), py = Math.sin(a), nx = -py, ny = px;
      const pts = [
        [cx + px * thisTipR, cy + py * thisTipR],
        [cx + px * baseR + nx * halfW, cy + py * baseR + ny * halfW],
        [cx + px * baseR - nx * halfW, cy + py * baseR - ny * halfW],
      ].map(([x, y]) => `${x.toFixed(2)},${y.toFixed(2)}`).join(' ');

      const filled = state !== 'off';
      // The grade itself is the most useful thing the tooltip can say — "MCP
      // Server: derived" is a different fact from "MCP Server: satisfied", and
      // telling them apart is the entire point of 0.6.
      const detail = typeof raw === 'string' && raw !== 'true'
        ? raw
        : (state === 'off' ? 'not satisfied' : 'satisfied');

      parts.push(
        `<polygon points="${pts}" ` +
        (filled ? `fill="${rayCol}" stroke="${rayCol}" stroke-width="${(strokeW * 0.5).toFixed(2)}"`
                : `fill="none" stroke="${C.rayOff}" stroke-width="${strokeW.toFixed(2)}"`) +
        ` stroke-linejoin="round" data-kind="ray" data-label="${esc(d.label)}" ` +
        `data-on="${filled}" data-state="${state}">` +
        `<title>${esc(d.label)}: ${esc(detail)}</title></polygon>`);
    });
  }

  // --- core ---------------------------------------------------------------
  // The disc sits INSIDE the innermost ring (radius coreR, not coreR + gap).
  // At coreR + gap it covered 83% of that ring, hiding Commercial Clarity and
  // swallowing its hover. pointer-events="none" so it can never block a ring.
  const scoreBand = p.band || bandOf(p.score);
  parts.push(
    `<circle cx="${cx}" cy="${cy}" r="${coreR.toFixed(2)}" ` +
    `fill="${opts.coreFill || C.surface}" pointer-events="none"/>`);

  if (size >= 96) {
    const withBand = palette === 'facet';
    parts.push(
      `<text x="${cx}" y="${(cy - (withBand ? size * 0.020 : 0)).toFixed(1)}" ` +
      `text-anchor="middle" dominant-baseline="central" pointer-events="none" ` +
      `font-family="system-ui,-apple-system,Segoe UI,sans-serif" font-weight="700" ` +
      `font-size="${(size * 0.130).toFixed(1)}" fill="${C.ink}">${Number(p.score).toFixed(1)}</text>`);
    if (withBand) {
      // Rank left the rings, so state it plainly under the number.
      parts.push(
        `<text x="${cx}" y="${(cy + size * 0.064).toFixed(1)}" text-anchor="middle" ` +
        `dominant-baseline="central" pointer-events="none" ` +
        `font-family="system-ui,-apple-system,Segoe UI,sans-serif" font-weight="600" ` +
        `font-size="${(size * 0.038).toFixed(1)}" fill="${C.muted}" ` +
        `letter-spacing="${(size * 0.003).toFixed(2)}">${scoreBand.toUpperCase()}</text>`);
    }
  } else {
    parts.push(
      `<circle cx="${cx}" cy="${cy}" r="${(coreR * 0.55).toFixed(2)}" ` +
      `fill="${PALETTES.ordinal[mode][scoreBand]}" pointer-events="none"/>`);
  }

  const label = opts.title || `${p.name}: Kin Score ${Number(p.score).toFixed(1)} (${scoreBand}), ` +
    `agent readiness ${Number(p.agent_score || 0).toFixed(0)} (${p.agent_band || 'human-only'})`;

  return `<svg viewBox="0 0 ${size} ${size}" width="${size}" height="${size}" ` +
    `xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${esc(label)}">` +
    `<title>${esc(label)}</title>${parts.join('')}</svg>`;
}


  function parseJSONAttr(el, name) {
    const raw = el.getAttribute(name);
    if (!raw) return {};
    try { return JSON.parse(raw); } catch (e) { return {}; }
  }

  /* Facets accept either a keyed object or a COMPACT array in FACETS order:
       data-facets='[67.5,61.8,73.7,94.7,84.8,76.3]'
     The compact form exists because the apis.io listing payload carries every
     provider in the network — keyed objects doubled that file. */
  function readFacets(el) {
    const v = parseJSONAttr(el, 'data-facets');
    if (!Array.isArray(v)) return v;
    const out = {};
    for (let i = 0; i < FACETS.length; i++) out[FACETS[i].id] = Number(v[i]) || 0;
    return out;
  }

  /* Dimensions accept a keyed object or a COMPACT TRIT STRING in DIMENSIONS
     order:  '0' unsatisfied, '1' satisfied, '2' PARTIAL.  data-dims='11020120...'

     '2' is the 0.6 addition. '1' deliberately keeps its old meaning so an
     encoding written before 0.6 still renders correctly rather than silently
     demoting every satisfied dimension to a stub. Keyed objects may instead
     carry the grade verbatim ('verified', 'documented', 'derived'), which is
     what provider frontmatter does — rayState() normalizes either form. */
  function readDims(el) {
    const raw = el.getAttribute('data-dims');
    if (raw && /^[012]+$/.test(raw.trim())) {
      const bits = raw.trim(), out = {};
      for (let i = 0; i < DIMENSIONS.length; i++) out[DIMENSIONS[i].id] = bits.charAt(i);
      return out;
    }
    return parseJSONAttr(el, 'data-dims');
  }

  /** Render one placeholder element in place. */
  function render(el) {
    if (el.getAttribute('data-kin-rendered') === '1') return;
    const p = {
      name:        el.getAttribute('data-name') || '',
      score:       parseFloat(el.getAttribute('data-score') || '0') || 0,
      band:        el.getAttribute('data-band') || null,
      agent_score: parseFloat(el.getAttribute('data-agent-score') || '0') || 0,
      agent_band:  el.getAttribute('data-agent-band') || 'human-only',
      facets:      readFacets(el),
      agent_dims:  readDims(el),
    };
    const size = parseInt(el.getAttribute('data-size') || '72', 10);
    const mode = el.getAttribute('data-mode') ||
      (document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light');
    el.innerHTML = kinGlyph(p, {
      size: size,
      mode: mode,
      palette: el.getAttribute('data-palette') || 'facet',
      showRays: el.getAttribute('data-rays') !== 'false',
      coreFill: el.getAttribute('data-core-fill') || undefined,
    });
    el.setAttribute('data-kin-rendered', '1');
  }

  function renderAll(scope) {
    const nodes = (scope || document).querySelectorAll('[data-kin-glyph]');
    for (let i = 0; i < nodes.length; i++) render(nodes[i]);
    return nodes.length;
  }

  root.KinGlyph = {
    render: render,
    renderAll: renderAll,
    svg: kinGlyph,
    FACETS: FACETS,
    DIMENSIONS: DIMENSIONS,
    BANDS: BANDS,
    PALETTES: PALETTES,
    RAYS: RAYS,
    bandOf: bandOf,
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { renderAll(); });
  } else {
    renderAll();
  }
})(typeof window !== 'undefined' ? window : globalThis);
