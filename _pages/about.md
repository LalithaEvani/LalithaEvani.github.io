---
layout: about
title: about
permalink: /

profile:
  align: right
  image: prof_pic.png # TODO: temporary illustrated placeholder — swap for a real photo (see assets/img/prof_pic.png)
  more_info: >
    <p>IIIT Hyderabad</p>
    <p>Gachibowli, Hyderabad 500032</p>
    <p>India</p>

selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false

latest_posts:
  enabled: false
---

Hi 👋 I'm an MS by Research student at the Centre for Visual Information
Technology (CVIT), IIIT Hyderabad, working with Prof. C.V. Jawahar and
Dr. Ajoy Mondal on Optical Character Recognition (OCR), with a focus on
Indic handwritten text recognition (Indic HTR).

During my MS, I've been working on representation learning, and found myself
especially drawn to how unlabelled data and math can be used to get a model
learning without labels, in a semi- or self-supervised fashion. I was initially
drawn to the math underlying machine learning, and over time I started liking
the applied research side of computer vision and AI just as much. It's
fascinating how applied math can be used in ML, and how ML can in turn be used
in applied research to solve real-world problems.

Going forward, I'm looking for industrial research roles in CV/ML, with a
particular interest in AI for Social Good.

Outside the lab, you'll find me with a cup of chai, a book, or a paintbrush.
I'm always open to making new friends, understanding different perspectives,
and slowly working out the philosophy of life.

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

