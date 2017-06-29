d3.selectAll('.item')
  .text("proto human")
  .classed("human", true)
  .style('background', function(d,i){
      return 'rgb(' + i*42 + ',128,128)'
  })
  


var n = 0;

function anim() {
    window.requestAnimationFrame(anim);

    d3.select('.item:nth-child(3)')
      .style('background', 'rgb(' + n + ',128,128)')
    n += 1;
    if(n > 255) n = 0;
    
    //console.log(n)
}

//window.requestAnimationFrame(anim);