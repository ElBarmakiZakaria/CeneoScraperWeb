function styleit(){
    const searchBar = document.getElementById("search-bar")
    

    var newDiv = document.createElement('div');
    newDiv.className = 'spinner-border text-primary';
    newDiv.setAttribute('role', 'status');
    newDiv.style.marginTop = "40px";

    var innerSpan = document.createElement('span');
    innerSpan.className = 'visually-hidden';
    innerSpan.textContent = 'Loading...';

    newDiv.appendChild(innerSpan);

    searchBar.appendChild(newDiv);

}



fetch('/productdata')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    
    myFunction(data);
  })
  .catch(error => {
    console.error('Error:', error);
  });

function myFunction(data){
    pieGraph(data[0])
    bargraph(data[1])
    
}




function pieGraph(results){
    const ctx = document.getElementById('pie-graph');
  
    new Chart(ctx, {
        type: 'doughnut',
        data: {
        labels: [
            'rocommended',
            'not-recommended',
            'null'
        ],
        datasets: [{
          label: 'Recommendation',
          data: results,
          backgroundColor: [
          'rgb(0, 200, 255)',
          'rgb(255, 99, 132)',
          'rgb(255, 205, 86)'
          ],
          hoverOffset: 5,
          hoverBackgroundColor: [
            'rgb(0, 100, 222)',
            'rgb(186, 0, 39)',
            'rgb(213, 184, 0)'
            ]
          
    }]
        },
        options: {}
    });
  }
  
  function bargraph(results){
    const ctx = document.getElementById('bar-graph');
  
    new Chart(ctx, {
        type: 'bar',
        data: {
        labels: [
            '0,0',
            '0,5',
            '1,0',
            '1,5',
            '2,0',
            '2,5',
            '3,0',
            '3,5',
            '4,0',
            '4,5',
            '5'
        ],
        datasets: [{
          
          label: 'Score',
          data: results,
          backgroundColor: [
            'rgba(255, 205, 86, 0.6)',
            'rgba(255, 205, 86, 0.6)',
            'rgba(255, 205, 86, 0.6)',
            'rgba(255, 205, 86, 0.6)',
            'rgba(255, 205, 86, 0.6)',
            'rgba(255, 205, 86, 0.6)',
            'rgba(255, 205, 86, 0.6)',
            'rgba(255, 205, 86, 0.6)',
            'rgba(255, 205, 86, 0.6)',
            'rgba(255, 205, 86, 0.6)',
            'rgba(255, 205, 86, 0.6)'
          ],
          hoverOffset: 5,
          hoverBackgroundColor: [
            'rgb(255, 205, 86)',
            'rgb(255, 205, 86)',
            'rgb(255, 205, 86)',
            'rgb(255, 205, 86)',
            'rgb(255, 205, 86)',
            'rgb(255, 205, 86)',
            'rgb(255, 205, 86)',
            'rgb(255, 205, 86)',
            'rgb(255, 205, 86)',
            'rgb(255, 205, 86)',
            'rgb(255, 205, 86)'
            ],
          borderWidth: 1
          
    }]
        },
        options: {
          
          plugins: {
            legend: {
              display: false
            }
          }
        }
    });
  }