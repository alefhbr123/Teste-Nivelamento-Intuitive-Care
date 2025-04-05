<template>
  <div>
    <h2>Busca de Operadoras</h2>
    <input v-model="searchQuery" @input="search" placeholder="Digite o nome ou termo de busca" />
    <ul>
      <li v-for="operadora in operadoras" :key="operadora.cnpj">
        {{ operadora.nome_operadora }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: "",
      operadoras: []
    };
  },
  methods: {
    search() {
      // Faz uma requisição para a API passando o termo de busca.
      fetch(`http://localhost:5000/api/operadoras?q=${this.searchQuery}`)
        .then(response => response.json())
        .then(data => {
          this.operadoras = data;
        })
        .catch(err => console.error("Erro na busca:", err));
    }
  },
  mounted() {
    // Carrega os dados ao montar o componente.
    this.search();
  }
};
</script>

<style scoped>
input {
  margin-bottom: 10px;
  padding: 5px;
  width: 300px;
}
</style>
