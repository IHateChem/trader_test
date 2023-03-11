function drawGraph(selector, json) {
  // Create SVG element
  var svg = d3.select(selector)
              .append("svg")
              .attr("width", 600)
              .attr("height", 400);

  // Define the data for the nodes and edges
  var nodes = json.nodes;
  var links = json.links;

  // Set up the simulation
  var simulation = d3.forceSimulation(nodes)
                     .force("link", d3.forceLink(links).id(function(d) { return d.id; }))
                     .force("charge", d3.forceManyBody())
                     .force("center", d3.forceCenter(300, 200));

  // Add the links
  var link = svg.append("g")
                .selectAll("line")
                .data(links)
                .enter()
                .append("line")
                .attr("stroke", "#999")
                .attr("stroke-width", "1px");

  // Add the nodes
  var node = svg.append("g")
                .selectAll("circle")
                .data(nodes)
                .enter()
                .append("circle")
                .attr("r", 10)
                .attr("fill", "#2c3e50");

  // Add the labels
  var label = svg.append("g")
                 .selectAll("text")
                 .data(nodes)
                 .enter()
                 .append("text")
                 .text(function(d) { return d.id; })
                 .attr("font-size", "12px")
                 .attr("dx", 12)
                 .attr("dy", 4);

  // Define the tick function to update the positions of the nodes and edges
  function ticked() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node.attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });

    label.attr("x", function(d) { return d.x; })
         .attr("y", function(d) { return d.y; });
  }

  // Start the simulation
  simulation.on("tick", ticked);
}
