deleteVenue = id => {
        return fetch(`/venues/${id}`,
            {method: 'DELETE'
            })
    }