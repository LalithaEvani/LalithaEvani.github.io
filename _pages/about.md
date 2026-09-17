---
layout: about
title: about
permalink: /
subtitle: MS Researcher in Computer Vision & Machine Learning · <a href='https://www.iiit.ac.in/'>IIIT Hyderabad</a>

profile:
  align: right
  # image: prof_pic.jpg # no photo for now — uncomment and add assets/img/prof_pic.jpg to show one again
  more_info: >
    <p>IIIT Hyderabad</p>
    <p>Gachibowli, Hyderabad 500032</p>
    <p>India</p>

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false

latest_posts:
  enabled: false
---

<!-- TODO: replace this placeholder biography with your own. -->

I am a Master's researcher in **computer vision and machine learning** at
[IIIT Hyderabad](https://www.iiit.ac.in/). My research focuses on <!-- TODO: e.g.
representation learning for visual recognition, multimodal perception, efficient
deep models --> _(add a one-line description of your research interests here)_.

Before my MS, I <!-- TODO: brief background — undergrad, internships, prior work -->.
I am currently applying for **research positions** (PhD / research engineer / research
scientist roles) and am interested in <!-- TODO: topics or labs you'd like to work with -->.

On this site you can find my [publications](/publications/), a selection of
[projects](/projects/), and my [CV](/cv/). The quickest way to reach me is by
email — see the links below.

{%- if site.goatcounter_code %}
<!-- VISITOR COUNTER (GoatCounter). The first script records visits; the block
     below shows the running total as plain text styled to match the site.
     It stays hidden until the count loads, and hides silently on any error
     (e.g. before you enable the counter in GoatCounter's site settings). -->
<script data-goatcounter="https://{{ site.goatcounter_code }}.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
<div id="site-visits" class="text-center" style="margin-top:2.5rem;" hidden>
  <span style="font-size:0.75rem; letter-spacing:0.02em; color:var(--global-text-color-light, #828282);">
    <i class="fa-solid fa-eye" style="margin-right:0.4em; opacity:0.65;"></i><span id="site-visits-n"></span>&nbsp;visits
  </span>
</div>
<script>
  (function () {
    var box = document.getElementById("site-visits");
    if (!box) return;
    fetch("https://{{ site.goatcounter_code }}.goatcounter.com/counter/TOTAL.json")
      .then(function (r) { if (!r.ok) throw 0; return r.json(); })
      .then(function (d) {
        var n = parseInt(d.count, 10) || 0;
        if (n < 1) return; // don't show "0 visits" on a fresh site; lower this to 0 to always show
        document.getElementById("site-visits-n").textContent = n.toLocaleString();
        box.hidden = false;
      })
      .catch(function () {});
  })();
</script>
{%- endif %}

