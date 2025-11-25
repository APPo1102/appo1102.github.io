<template>
  <div
    class="BackgroundfadeIn flex h-[100vh] w-full flex-col items-center justify-center overflow-hidden bg-white dark:bg-black background wrapper"	
  >    
	<div class="fadeIn">
		<img src="./assets/main.png" style="opacity:0;">
	</div>
	<BlurReveal
      :delay="0.2"
      :duration="1"
      class="p-8"
    >
		<h2 class="text-2xl font-bold tracking-tighter xl:text-2xl/none sm:text-2xl Cactus mini-title">高訂品味 對味不凡</h2>
	</BlurReveal>
	<BlurReveal
      :delay="0.2"
      :duration="1"
      class="p-5 top-left"
    >
      <h2 class="text-2xl font-bold tracking-tighter xl:text-2xl/none sm:text-2xl title">水湳生態核心—限量４０席—２５坪法式寓邸</h2> 
    </BlurReveal>
	<BlurReveal
      :delay="0.2"
      :duration="1"
      class="p-5 top-right"
    >
	<h2 class="text-2xl font-bold tracking-tighter xl:text-2xl/none sm:text-2xl subtitle">Extraordinary Life</h2>
	</BlurReveal>
	<BlurReveal
      :delay="0.2"
      :duration="1"
      class="p-5 flex justify-content-between w-50 bottom"
    >
	<ShimmerButton
      class="shadow-2xl"
      shimmer-size="2px"
    >
      <span
        class="whitespace-pre-wrap text-center text-sm font-medium leading-none tracking-tight text-white lg:text-lg dark:from-white dark:to-slate-900/10 Cactus"
      >
        聚碩建築
      </span>
	</ShimmerButton>
	<ShimmerButton
      class="shadow-2xl"
      shimmer-size="2px"
    >
	  <span
        class="whitespace-pre-wrap text-center text-sm font-medium leading-none tracking-tight text-white lg:text-lg dark:from-white dark:to-slate-900/10 Cactus"
      >
        璀璨國際
      </span>
	 </ShimmerButton>
	<ShimmerButton
      class="shadow-2xl"
      shimmer-size="2px"
    >
	  <span
        class="whitespace-pre-wrap text-center text-sm font-medium leading-none tracking-tight text-white lg:text-lg dark:from-white dark:to-slate-900/10 Cactus"
      >
        法式寓邸
      </span>
	 </ShimmerButton>
	 
	<ShimmerButton
      class="shadow-2xl"
      shimmer-size="2px"
    >
	  <span
        class="whitespace-pre-wrap text-center text-sm font-medium leading-none tracking-tight text-white lg:text-lg dark:from-white dark:to-slate-900/10 Cactus"
      >
        雋刻心藝
      </span>
    </ShimmerButton>
	</BlurReveal>
  </div>   
  <SleekLineCursor />
  
</template>
<script setup lang="ts">
import { computed } from "vue";
import { useColorMode } from "@vueuse/core";
import BlurReveal from "./components/ui/blur-reveal/BlurReveal.vue"
import ShimmerButton from "./components/ui/shimmer-button/ShimmerButton.vue"
// @ts-ignore
const particlesColor = computed(() => (useColorMode().value === "dark" ? "#FFFFFF" : "#000000"));
</script>
<style>

.fadeIn {  
  background: url(./assets/main.png);
  mask-image: linear-gradient(to bottom, transparent 0%, transparent 100%);
  background-size: cover;
  mask-repeat: no-repeat;
  width:70%;
  background-repeat: no-repeat;
  animation: fadeInFromTop 2s forwards; 
}
.BackgroundfadeIn{  
  animation: fadeIn 2s forwards; 
}
@keyframes fadeIn {
  0% {    
	opacity: 0.6;	
  }  
  100%{	
	opacity: 1;	
  }
}
@keyframes fadeInFromTop {
  0%   {opacity:0; mask-image: linear-gradient(to bottom, black 0%, transparent 0%); }
1%   { mask-image: linear-gradient(to bottom, black 1%, transparent 0%); }
2%   { mask-image: linear-gradient(to bottom, black 2%, transparent 0%); }
3%   { mask-image: linear-gradient(to bottom, black 3%, transparent 0%); }
4%   { mask-image: linear-gradient(to bottom, black 4%, transparent 0%); }
5%   { mask-image: linear-gradient(to bottom, black 5%, transparent 0%); }
6%   { mask-image: linear-gradient(to bottom, black 6%, transparent 0%); }
7%   { mask-image: linear-gradient(to bottom, black 7%, transparent 0%); }
8%   { mask-image: linear-gradient(to bottom, black 8%, transparent 0%); }
9%   { mask-image: linear-gradient(to bottom, black 9%, transparent 0%); }
10%  { mask-image: linear-gradient(to bottom, black 10%, transparent 0%); }
11%  { mask-image: linear-gradient(to bottom, black 11%, transparent 0%); }
12%  { mask-image: linear-gradient(to bottom, black 12%, transparent 0%); }
13%  { mask-image: linear-gradient(to bottom, black 13%, transparent 0%); }
14%  { mask-image: linear-gradient(to bottom, black 14%, transparent 0%); }
15%  { mask-image: linear-gradient(to bottom, black 15%, transparent 0%); }
16%  { mask-image: linear-gradient(to bottom, black 16%, transparent 0%); }
17%  { mask-image: linear-gradient(to bottom, black 17%, transparent 0%); }
18%  { mask-image: linear-gradient(to bottom, black 18%, transparent 0%); }
19%  { mask-image: linear-gradient(to bottom, black 19%, transparent 0%); }
20%  { mask-image: linear-gradient(to bottom, black 20%, transparent 0%); }
21%  { mask-image: linear-gradient(to bottom, black 21%, transparent 0%); }
22%  { mask-image: linear-gradient(to bottom, black 22%, transparent 0%); }
23%  { mask-image: linear-gradient(to bottom, black 23%, transparent 0%); }
24%  { mask-image: linear-gradient(to bottom, black 24%, transparent 0%); }
25%  { mask-image: linear-gradient(to bottom, black 25%, transparent 0%); }
26%  { mask-image: linear-gradient(to bottom, black 26%, transparent 0%); }
27%  { mask-image: linear-gradient(to bottom, black 27%, transparent 0%); }
28%  { mask-image: linear-gradient(to bottom, black 28%, transparent 0%); }
29%  { mask-image: linear-gradient(to bottom, black 29%, transparent 0%); }
30%  { mask-image: linear-gradient(to bottom, black 30%, transparent 0%); }
31%  { mask-image: linear-gradient(to bottom, black 31%, transparent 0%); }
32%  { mask-image: linear-gradient(to bottom, black 32%, transparent 0%); }
33%  { mask-image: linear-gradient(to bottom, black 33%, transparent 0%); }
34%  { mask-image: linear-gradient(to bottom, black 34%, transparent 0%); }
35%  { mask-image: linear-gradient(to bottom, black 35%, transparent 0%); }
36%  { mask-image: linear-gradient(to bottom, black 36%, transparent 0%); }
37%  { mask-image: linear-gradient(to bottom, black 37%, transparent 0%); }
38%  { mask-image: linear-gradient(to bottom, black 38%, transparent 0%); }
39%  { mask-image: linear-gradient(to bottom, black 39%, transparent 0%); }
40%  { mask-image: linear-gradient(to bottom, black 40%, transparent 0%); }
41%  { mask-image: linear-gradient(to bottom, black 41%, transparent 0%); }
42%  { mask-image: linear-gradient(to bottom, black 42%, transparent 0%); }
43%  { mask-image: linear-gradient(to bottom, black 43%, transparent 0%); }
44%  { mask-image: linear-gradient(to bottom, black 44%, transparent 0%); }
45%  { mask-image: linear-gradient(to bottom, black 45%, transparent 0%); }
46%  { mask-image: linear-gradient(to bottom, black 46%, transparent 0%); }
47%  { mask-image: linear-gradient(to bottom, black 47%, transparent 0%); }
48%  { mask-image: linear-gradient(to bottom, black 48%, transparent 0%); }
49%  { mask-image: linear-gradient(to bottom, black 49%, transparent 0%); }
50%  { mask-image: linear-gradient(to bottom, black 50%, transparent 0%); }
51%  { mask-image: linear-gradient(to bottom, black 51%, transparent 0%); }
52%  { mask-image: linear-gradient(to bottom, black 52%, transparent 0%); }
53%  { mask-image: linear-gradient(to bottom, black 53%, transparent 0%); }
54%  { mask-image: linear-gradient(to bottom, black 54%, transparent 0%); }
55%  { mask-image: linear-gradient(to bottom, black 55%, transparent 0%); }
56%  { mask-image: linear-gradient(to bottom, black 56%, transparent 0%); }
57%  { mask-image: linear-gradient(to bottom, black 57%, transparent 0%); }
58%  { mask-image: linear-gradient(to bottom, black 58%, transparent 0%); }
59%  { mask-image: linear-gradient(to bottom, black 59%, transparent 0%); }
60%  { mask-image: linear-gradient(to bottom, black 60%, transparent 0%); }
61%  { mask-image: linear-gradient(to bottom, black 61%, transparent 0%); }
62%  { mask-image: linear-gradient(to bottom, black 62%, transparent 0%); }
63%  { mask-image: linear-gradient(to bottom, black 63%, transparent 0%); }
64%  { mask-image: linear-gradient(to bottom, black 64%, transparent 0%); }
65%  { mask-image: linear-gradient(to bottom, black 65%, transparent 0%); }
66%  { mask-image: linear-gradient(to bottom, black 66%, transparent 0%); }
67%  { mask-image: linear-gradient(to bottom, black 67%, transparent 0%); }
68%  { mask-image: linear-gradient(to bottom, black 68%, transparent 0%); }
69%  { mask-image: linear-gradient(to bottom, black 69%, transparent 0%); }
70%  { mask-image: linear-gradient(to bottom, black 70%, transparent 0%); }
71%  { mask-image: linear-gradient(to bottom, black 71%, transparent 0%); }
72%  { mask-image: linear-gradient(to bottom, black 72%, transparent 0%); }
73%  { mask-image: linear-gradient(to bottom, black 73%, transparent 0%); }
74%  { mask-image: linear-gradient(to bottom, black 74%, transparent 0%); }
75%  { mask-image: linear-gradient(to bottom, black 75%, transparent 0%); }
76%  { mask-image: linear-gradient(to bottom, black 76%, transparent 0%); }
77%  { mask-image: linear-gradient(to bottom, black 77%, transparent 0%); }
78%  { mask-image: linear-gradient(to bottom, black 78%, transparent 0%); }
79%  { mask-image: linear-gradient(to bottom, black 79%, transparent 0%); }
80%  { mask-image: linear-gradient(to bottom, black 80%, transparent 0%); }
81%  { mask-image: linear-gradient(to bottom, black 81%, transparent 0%); }
82%  { mask-image: linear-gradient(to bottom, black 82%, transparent 0%); }
83%  { mask-image: linear-gradient(to bottom, black 83%, transparent 0%); }
84%  { mask-image: linear-gradient(to bottom, black 84%, transparent 0%); }
85%  { mask-image: linear-gradient(to bottom, black 85%, transparent 0%); }
86%  { mask-image: linear-gradient(to bottom, black 86%, transparent 0%); }
87%  { mask-image: linear-gradient(to bottom, black 87%, transparent 0%); }
88%  { mask-image: linear-gradient(to bottom, black 88%, transparent 0%); }
89%  { mask-image: linear-gradient(to bottom, black 89%, transparent 0%); }
90%  { mask-image: linear-gradient(to bottom, black 90%, transparent 0%); }
91%  { mask-image: linear-gradient(to bottom, black 91%, transparent 0%); }
92%  { mask-image: linear-gradient(to bottom, black 92%, transparent 0%); }
93%  { mask-image: linear-gradient(to bottom, black 93%, transparent 0%); }
94%  { mask-image: linear-gradient(to bottom, black 94%, transparent 0%); }
95%  { mask-image: linear-gradient(to bottom, black 95%, transparent 0%); }
96%  { mask-image: linear-gradient(to bottom, black 96%, transparent 0%); }
97%  { mask-image: linear-gradient(to bottom, black 97%, transparent 0%); }
98%  { mask-image: linear-gradient(to bottom, black 98%, transparent 0%); }
99%  { mask-image: linear-gradient(to bottom, black 99%, transparent 0%); }
100% { opacity:1; mask-image: linear-gradient(to bottom, black 100%, transparent 0%); }

}
@font-face {
  font-family: 'Cactus'; /* Define a name for your font */
  src: url('CactusClassicalSerif-Regular.ttf') format('ttf');       
  font-weight: normal;
  font-style: normal;
}

.title{
	background-image: linear-gradient(#FFFFDF, #BA8E43);
    color: transparent;
    background-clip: text;	
	line-height: 1.5;	
	opacity:0.8;
	font-family: 'Cactus';	
	font-weight:600;
}

.subtitle{
	background-image: linear-gradient(#FFFFDF, #BA8E43);
    color: transparent;
    background-clip: text;
	letter-spacing:10px;
	writing-mode: sideways-lr;
	text-orientation: upright;
	opacity:0.6;
	font-family: 'Cactus';	
	font-weight:600;
}

.mini-title{
	background-image: linear-gradient(#FFFFDF, #BA8E43);
    color: transparent;
    background-clip: text;	
	letter-spacing:20px;
	font-size:48px;
	font-weight:200;
}

.align-center{
	text-align:center;
}

.background{
	background:url(./assets/background.jpg);
	background-size: cover;
	background-repeat: no-repeat;
}

.wrapper {
  position: relative;
  min-height: 300px;
}

.top-left {
  position: absolute;
  width:64px;
  top: 0;
  left: 0;
}

.top-right {
  position: absolute;  
  top: 0;
  right: 0;
}

.d-flex{
	display:flex;
}
.justify-content-between{
	justify-content:space-between;
}
.w-50{
	width: 50%;
}
.Cactus{
	font-family: Cactus;	
	font-weight: 200;
}
.bottom{
	position: absolute;
	bottom:0;
}
</style>