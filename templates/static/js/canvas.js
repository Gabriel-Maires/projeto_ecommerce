function retorna_total_vendido(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('lucro_total').innerHTML = 'R$ '+ data.data
    })
}

function renderiza_faturamento_mensais(url){

    fetch(url, {
        method: 'GET',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        data_faturamento = data.data
        data_despesas = data.data_despesas 
        labels = data.labels
        lucro = data.lucro

        const ctx = document.getElementById('faturamento_mensal').getContext("2d");

        const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Faturamento mensal',
                    backgroundColor: ['blue',],
                    data: data_faturamento,
                    borderWidth: 1
                },
                {
                    label: 'Despesa mensal',
                    backgroundColor: ['rgba(255, 205, 86, 1)',],
                    data: data_despesas,
                    borderWidth: 1
                },
                    ],
                },
        });

        const ctx2 = document.getElementById('lucro').getContext("2d");

        const chart_lucro = new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
            label: 'lucro',
            backgroundColor: ['green',],
            data: lucro,
            borderWidth: 1
            }]
        },
        });
    })   
}

function relatorio_produtos(url){

    fetch(url, {
        method: 'GET',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        y = data.data
        x = data.labels

        const ctx = document.getElementById('relatorio_produtos').getContext("2d");

        const chart_produtos = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: x,
            datasets: [{
            label: 'Faturamento total',
            data: y,
            borderWidth: 0.5
            }]
        },
        options: {
            responsive: true,
            scales: {
            y: {
                beginAtZero: true
            }
            }
        }
    })
}) 
}

// Talvez seja melhor deixar dois ou um só fetch